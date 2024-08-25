train_model is the code for training the BART model with the modified dataset. main.py will hold the simulation. dataset_modification.py 
holds code for modifying the menghor dataset. test.py is for testing datasets and models for whatever reason. The modified dataset is 
held in the folder called modified_dataset. The trained model is held in the trained_model folder.

This is a link for our original dataset: https://huggingface.co/datasets/menghor/navigation_robotic_instruct 
This is another dataset just in case: https://huggingface.co/datasets/Aryaduta/llm_robot?row=17
Bart-base model: https://huggingface.co/facebook/bart-base

Some notes:
# Default speed and distance is 1 meter/sec and 1 meter.
# Default rotation is 90 degrees in any direction on a 2d, horizontal plane, with angular velocity of 90.
# Default direction of roation will be clockwise.
# Deploying this model requires different code from simulation to deal with specific degree rotation.
# Add in sequences (will be longer)
# Issue: long responses will be cut off, sequences will most likely be cut off.
# Issue: default distance is not 1 for some reason