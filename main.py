from datasets import load_dataset

# Load the dataset
# Load the dataset
dataset = load_dataset('Aryaduta/llm_robot')

# Print a sample to inspect the response field
for example in dataset['train']:
    print("Sample input:", example['input'])
    print("Sample response:", example['response'])
    break

