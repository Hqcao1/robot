from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# Default speed and distance is 1 meter/sec and 1 meter.
# Default rotation is 90 degrees in any direction on a 2d, horizontal plane, with angular velocity of 90.
# Default direction of roation will be clockwise.
# Deploying this model requires different code from simulation to deal with specific degree rotation.
# Delete all rows with keywords: up, rise, propel, climb, ascend, down, downward, downwards, go to, take, snap, capture, photo, shoot, water
#   drink, take, hydrate, robot, RosGPT, bedroom, room
# Add in sequences (will be longer)
# Issue: long responses will be cut off, sequences will most likely be cut off.
# Issue: default distance appears to have changed to 2 meters for some reason.

model_path = './trained_model'  
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

