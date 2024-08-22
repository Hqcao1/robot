The llm_robot.py file is the code that trained the current model with Aryaduta/llm_robot. navigation_robotic_instruct uses another dataset 
that is a modified menghor set, it is missing some commands for sequence. main.py will hold the simulation. dataset_modification.py 
holds code for modifying the menghor dataset. test.py is for testing datasets and models fow whatever reason. The modified dataset is 
held in the folder called modified_dataset. 

This is a link for our original dataset: https://huggingface.co/datasets/menghor/navigation_robotic_instruct 
This is secondary: https://huggingface.co/datasets/Aryaduta/llm_robot?row=17
Bart-base model: https://huggingface.co/facebook/bart-base

Some notes:
 -The model seems to be able to process simple commands, but longer ones get cut off.
 -Using another model might be the move

# Default speed and distance is 1 meter/sec and 1 meter.
# Default rotation is 90 degrees in any direction on a 2d, horizontal plane, with angular velocity of 90.
# Default direction of roation will be clockwise.
# Deploying this model requires different code from simulation to deal with specific degree rotation.
# Delete all rows with keywords: up, rise, propel, climb, ascend, down, downward, downwards, go to, take, snap, capture, photo, shoot, water
#   drink, take, hydrate, robot, RosGPT, bedroom, room
# Add in sequences (will be longer)
# Issue: long responses will be cut off, sequences will most likely be cut off.
# Issue: default distance appears to have changed to 2 meters for some reason.