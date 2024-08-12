from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
import evaluate
import numpy as np
import torch
import json

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelForSeq2SeqLM.from_pretrained('t5-small')

# Enable gradient checkpointing to save memory
model.gradient_checkpointing_enable()

# Load the accuracy metric
metric = evaluate.load('accuracy')

# Tokenization function with JSON extraction
def tokenize_function(examples):
    instructions = examples['input']
    responses = [
        json.dumps({
            "actions": [
                {
                    "command": action['command'],
                    "parameters": {
                        "x": action['parameters'].get('x', None),
                        "y": action['parameters'].get('y', None),
                        "z": action['parameters'].get('z', None),
                        "action": action['parameters'].get('action', None),
                        "direction": action['parameters'].get('direction', None),
                        "msg": action['parameters'].get('msg', None)
                    }
                } for action in resp['actions']
            ]
        })
        for resp in examples['response']
    ]
    
    model_inputs = tokenizer(instructions, padding='max_length', truncation=True, max_length=128)
    labels = tokenizer(responses, padding='max_length', truncation=True, max_length=128)
    
    model_inputs['labels'] = labels['input_ids']
    return model_inputs

# Compute metrics function
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    
    # Ensure predictions are token IDs
    if isinstance(predictions, tuple):
        predictions = predictions[0]
    
    # Convert predictions to token IDs using argmax
    predictions = torch.argmax(torch.tensor(predictions), dim=-1)
    
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Simple string comparison for accuracy
    accuracy = np.mean([pred.strip() == label.strip() for pred, label in zip(decoded_preds, decoded_labels)])
    
    return {'accuracy': accuracy}

# Load dataset
dataset = load_dataset('Aryaduta/llm_robot')

# Tokenize the dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=['input', 'response'])

# Split the dataset into train and test sets
split_dataset = tokenized_datasets['train'].train_test_split(test_size=0.2)

# Define data collator
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# Define training arguments
training_args = TrainingArguments(
    output_dir='test_trainer',
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=16,
    num_train_epochs=5,
    weight_decay=0.01,
    fp16=True,
    logging_dir='logs',
    logging_steps=10,
    save_total_limit=3,
    load_best_model_at_end=True,
    metric_for_best_model='accuracy',
    greater_is_better=True
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=split_dataset['train'],
    eval_dataset=split_dataset['test'],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)

# Train the model
trainer.train()

# Save the model and tokenizer
trainer.save_model("test_trainer")
tokenizer.save_pretrained("test_trainer")

# Load the model and tokenizer later
loaded_tokenizer = AutoTokenizer.from_pretrained("test_trainer")
loaded_model = AutoModelForSeq2SeqLM.from_pretrained("test_trainer")

# Example usage of the loaded model
input_text = "Make the robot move to the forward direction four times"

# Tokenize the input text
inputs = loaded_tokenizer(input_text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)

# Generate predictions (greedy search)
outputs = loaded_model.generate(inputs['input_ids'], max_length=128)

# Decode the generated tokens to text
decoded_output = loaded_tokenizer.decode(outputs[0], skip_special_tokens=True)

# Ensure the output is in the correct JSON format
def validate_and_correct_json(output):
    try:
        parsed_output = json.loads(output)
        return json.dumps(parsed_output, indent=4)
    except json.JSONDecodeError:
        # Attempt to fix common JSON formatting issues
        output = output.replace("'", '"').replace("None", "null").strip()
        try:
            parsed_output = json.loads(output)
            return json.dumps(parsed_output, indent=4)
        except json.JSONDecodeError:
            return None

# Validate and correct the output
corrected_output = validate_and_correct_json(decoded_output)
if corrected_output:
    print("Corrected and parsed output:", corrected_output)
else:
    print("Output is not a valid JSON:", decoded_output)
