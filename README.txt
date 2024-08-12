The llm_robot.py file is the code that trained the current model with Aryaduta/llm_robot. navigation_robotic_instruct uses another dataset 
called menghor/navigation_robotic_instruct, it is missing some necessary commands. train3 uses Aryaduta as well but trains the t5-small model
instead of bart-base which we are currently using. test2.py is our main code to create the simulation and process commands with the model.
This is a link for our main dataset: https://huggingface.co/datasets/Aryaduta/llm_robot?row=17
This is secondary: https://huggingface.co/datasets/menghor/navigation_robotic_instruct
Bart-base model: https://huggingface.co/facebook/bart-base

Some notes:
 -The model seems to be able to process simple commands, but longer ones get cut off.
 -Using another model might be the move
 -Aryaduta dataset is probably fine for our purposes, but it is not exactly tailored to drone movement. 
    To get the model more accurate we might have to modify this dataset to remove robot arm movement, and add more drone explicit commands.