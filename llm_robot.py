from datasets import load_dataset
from transformers import AutoTokenizer, BartForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq
import numpy as np
import torch

# Load the dataset
dataset = load_dataset('Aryaduta/llm_robot')

# Tokenizer and Model
tokenizer = AutoTokenizer.from_pretrained('facebook/bart-base')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-base')

# Convert response dictionary to text, including null parameters
def response_to_text(response):
    actions = response.get('actions', [])
    actions_text = ' | '.join(
        f"Command: {action['command']}, Parameters: {', '.join(f'{k}: {v}' for k, v in action['parameters'].items())}"
        for action in actions
    )
    return actions_text

# Tokenization function with increased max_length and dynamic padding
def tokenize_function(examples):
    inputs = examples['input']
    outputs = [response_to_text(response) for response in examples['response']]
    model_inputs = tokenizer(inputs, max_length=128, padding='max_length', truncation=True)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(outputs, max_length=128, padding='max_length', truncation=True)
    
    model_inputs['labels'] = labels['input_ids']
    model_inputs['labels'] = [
        [(label if label != tokenizer.pad_token_id else -100) for label in labels_list] 
        for labels_list in model_inputs['labels']
    ]
    return model_inputs

# Tokenize the dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=['input', 'response'])

# Split the dataset into train and test sets
split_dataset = tokenized_datasets['train'].train_test_split(test_size=0.2)

# Use DataCollator for dynamic padding
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)

# Training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    save_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=3,
    load_best_model_at_end=True,
    logging_dir='./logs',
    logging_steps=10
)

# Metrics function
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    if isinstance(predictions, tuple):
        predictions = predictions[0]
    predictions = torch.tensor(predictions)
    predictions = torch.argmax(predictions, dim=-1).numpy()
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    labels = [[(label if label != -100 else tokenizer.pad_token_id) for label in l] for l in labels]
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    accuracy = np.mean([pred.strip() == label.strip() for pred, label in zip(decoded_preds, decoded_labels)])
    return {'accuracy': accuracy}

# Initialize the Trainer
trainer = Seq2SeqTrainer(
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
try:
    trainer.save_model('./trained_model')
    tokenizer.save_pretrained('./trained_model')
except Exception as e:
    print("Error during saving the model: ", e)
    trainer.save_model('./alternate_trained_model')
    tokenizer.save_pretrained('./alternate_trained_model')

# To use the model for predictions
input_text = "Shift the robot arm to go up direction."
inputs = tokenizer(input_text, return_tensors="pt", padding="max_length", truncation=True)
outputs = model.generate(inputs['input_ids'], max_length=128)
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated output:", decoded_output)
