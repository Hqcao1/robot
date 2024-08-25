from datasets import load_dataset, load_from_disk
from transformers import BartTokenizer, BartForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq
import numpy as np
import torch

# Load the dataset
dataset = load_from_disk('modified_set')

# Print dataset info
print("Dataset info:", dataset)

# Initialize the tokenizer and model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-base')

# Tokenization function
def tokenize_function(examples):
    inputs = examples['INPUT']
    outputs = examples['OUTPUT']
    model_inputs = tokenizer(inputs, max_length=128, padding='max_length', truncation=True)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(outputs, max_length=128, padding='max_length', truncation=True)
    
    model_inputs['labels'] = labels['input_ids']
    model_inputs['labels'] = [
        [(label if label != tokenizer.pad_token_id else -100) for label in labels] 
        for labels in model_inputs['labels']
    ]
    return model_inputs

# Tokenize the dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=['INPUT', 'OUTPUT'])

# Print tokenized dataset info
print("Tokenized dataset info:", tokenized_datasets)

# Split the dataset into train and test sets
split_dataset = tokenized_datasets['train'].train_test_split(test_size=0.2)

# Define data collator
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# Define training arguments
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

# Define compute_metrics function
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    if isinstance(predictions, tuple):
        predictions = predictions[0]
    
    # Ensure predictions are tensor before decoding
    predictions = torch.tensor(predictions)
    predictions = torch.argmax(predictions, dim=-1).numpy()

    # Decode predictions and labels
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    labels = [[(label if label != -100 else tokenizer.pad_token_id) for label in l] for l in labels]
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    
    # Simple string comparison for accuracy
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
trainer.save_model('./trained_model')
tokenizer.save_pretrained('./trained_model')