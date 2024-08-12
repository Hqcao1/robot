from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# Load the trained model and tokenizer
model_path = './trained_model'  # Ensure this is the correct path to your saved model
tokenizer = BartTokenizer.from_pretrained(model_path)
model = BartForConditionalGeneration.from_pretrained(model_path)

def parse_output(output):
    command_start = output.find("Command: ") + 9
    command_end = output.find(",", command_start)
    print(output[command_start:command_end])
    direction_start = output.find("direction: ") + 11
    direction_end = output.find(",", direction_start)
    print(output[direction_start:direction_end])

while True:
    command = input("Enter command: ")
    if command == "exit":
        exit()
    inputs = tokenizer(command, return_tensors="pt", padding="max_length", truncation=True, max_length=400)
    outputs = model.generate(inputs['input_ids'], max_length=400)
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    parse_output(decoded_output)
    print("Generated output:", decoded_output)

