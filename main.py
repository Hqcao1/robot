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
# Issue: default distance is not 1 for some reason

model_path = './trained_model'  
tokenizer = BartTokenizer.from_pretrained(model_path)
model = BartForConditionalGeneration.from_pretrained(model_path)

# Drone object to keep track of the location of the drone,
# the current direction the drone is facing, the speed of the
# drone, and the velocity at which the drone turn. Since this
# is a simple simulation, the speed, angular velocity, and z 
# does not matter. 0 = N, 1 = E, 2 = S, 3 = W
class Drone:
    def __init__(self, x, y, z, direction, speed, ang_velocity):
        self.x = x
        self.y = y
        self.z = z
        self.direction  = direction
        self.speed = speed
        self.ang_velocity = ang_velocity 
        
drone = Drone(3, 3, 0, 0, 1, 90)
        
# Draw the plot
def plot(drone):
    for y in range(6,-1,-1):
        for x in range(7):
            # Mark the drone
            if (x == drone.x) & (y == drone.y): 
                print("X", end =" ")
                continue
            print("O", end =" ")
        print()

# Change the coordinates of the drone
def exec_move(drone, speed, distance, direction):
    drone.speed = speed
    if direction == "backward":
        distance = -1 * int(distance)
    if drone.direction == 0:
        drone.y = drone.y + int(distance)
    elif drone.direction == 1:
        drone.x = drone.x + int(distance)
    elif drone.direction == 2:
        drone.y = drone.y - int(distance)
    elif drone.direction == 3:
        drone.x = drone.x - int(distance)
    # Check bounds of the grid
    if drone.y > 6:
        drone.y = 6
    if drone.y < 0:
        drone.y = 0
    if drone.x > 6:
        drone.x = 6
    if drone.x < 0:
        drone.x = 0
    
# Change the direction the drone is facing
def exec_turn(drone, ang_velocity, angle, direction):
    drone.ang_velocity = ang_velocity
    # For a 2d grid, the angles are assumed to be multiples of 90
    turns = int(angle) / 90 % 4 
    if direction == "right":
        drone.direction = (drone.direction + turns) % 4
    else:
        drone.direction = (drone.direction - turns) % 4
        
# Take the decoded output from the model to execute drone commands
def parse_output(output):
    
    # Move the drone
    if output.find("move") != -1:
        speed = output[output.find("linear_speed") + 15: output.find("," ,output.find("linear_speed") + 15)]
        distance = output[output.find("distance") + 11: output.find(",", output.find("distance") + 11)]
        direction = ""
        if output.find("is_forward") != -1:
            if output.find("true") != -1:
                direction = "forward"
            else:
                direction = "backward"
        else:
            if output.find("true") != -1:
                direction = "upward"
            else:
                direction = "downward"
        exec_move(drone, speed, distance, direction)
        
    # Turn the drone
    elif output.find("rotate") != -1:
        ang_velocity = output[output.find("angular_velocity") + 19: output.find("," ,output.find("angular_velocity") + 19)]
        angle = output[output.find("angle") + 8: output.find(",", output.find("angle") + 8)]
        direction = ""
        if output.find("is_clockwise") != -1:
            if output.find("true") != -1:
                direction = "right"
            else:
                direction = "left"
        exec_turn(drone, ang_velocity, angle, direction)
        
    # Execute a sequence of commands (In Progress)
    elif output.find("sequence") != -1:
        print("sequence")
        
    # Something went wrong with the model
    else:
        print("error")

# Loop to take in commands continually
while True:
    plot(drone)
    command = input("Enter command: ")
    if command == "exit":
        exit()
        
    # Put the user input into the model to process
    inputs = tokenizer(command, return_tensors="pt", padding="max_length", truncation=True, max_length=400)
    outputs = model.generate(inputs['input_ids'], max_length=400)
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    parse_output(decoded_output)
    print("Generated output:", decoded_output)