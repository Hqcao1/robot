from datasets import load_dataset, load_from_disk, concatenate_datasets, DatasetDict, Dataset

dataset = load_from_disk('set')

print(dataset['train'])

dataset = load_from_disk('modified_set')

print(dataset)
