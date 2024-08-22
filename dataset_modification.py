from datasets import load_dataset, load_from_disk, concatenate_datasets, DatasetDict, Dataset

# Default speed and distance is 1 meter/sec and 1 meter.
# Default rotation is 90 degrees in any direction on a 2d, horizontal plane, with angular velocity of 90.
# Default direction of roation will be clockwise.
# Deploying this model requires different code from simulation to deal with specific degree rotation.
# Delete all rows with keywords: up, rise, propel, climb, ascend, down, downward, downwards, go to, take, snap, capture, photo, shoot, water
#   drink, take, hydrate, robot, RosGPT, bedroom, room
# Add in sequences (will be longer)
# Issue: long responses will be cut off, sequences will most likely be cut off.
# Issue: default distance appears to have changed to 2 meters for some reason.

# Load the dataset
dataset = load_from_disk('set')

print(dataset['train'])

#
# Delete all unecessary commands
list = ["up", "rise", "propel", "climb", "ascend", "down", "downward", "downwards", "go to", "take", "snap", "capture", "photo", "shoot", "water"
  "drink", "take", "hydrate", "robot", "RosGPT", "bedroom", "room"]

def filter_function(example):
    return not any(word in example['INPUT'].lower() for word in list)
dataset = dataset.filter(filter_function)

#
# Make default commands
# # # # # 

print(dataset['train'])

# Upward movement
list1 = [
    {'INPUT' : 'Move up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'}
]

# Downward movement
list2 = [
    {'INPUT' : 'Move down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'}
]

# Forward movement
list3 = [
    {'INPUT' : 'Move forward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'proceed', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'continue', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'move ahead', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'forge ahead', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'press on', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'push forward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'carry on', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'go forth', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'head forward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'go onward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'keep going', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'},
    {'INPUT' : 'go on', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": true, "unit": "meter" } }'}
]

# Backwards movement
list4 = [
    {'INPUT' : 'Move backward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'retreat', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'reverse', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'back up', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'recede', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'withdraw', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'backtrack', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'back pedal', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'move back', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'step back', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'back away', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall back', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'pull back', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in reverse', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'move rearward', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'},
    {'INPUT' : 'move backwardly', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_forward": false, "unit": "meter" } }'}
]

# Rotation
list5 = [
    {'INPUT' : 'rotate', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'rotate right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'rotate left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'rotate clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'rotate counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'turn', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'turn right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'turn left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'turn clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'turn counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'spin', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'spin right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'spin left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'spin clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'spin counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'swivel', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'swivel right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'swivel left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'swivel clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'swivel counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'pivot', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'pivot right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'pivot left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'pivot clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'pivot counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'circle', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'circle right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'circle left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'circle clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'circle counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'swing', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'swing right', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'swing left', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'},
    {'INPUT' : 'swing clockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": true, "unit": "degrees" } }'},
    {'INPUT' : 'swing counterclockwise', 'OUTPUT': '{ "action": "rotate", "params": { "angular_velocity": 90, "angle": 90, "is_clockwise": false, "unit": "degrees" } }'}
]

# # # # #
# End of default commands
#

#
# Make upward and downward commands with measurements
# # # # #

# Upwards by 1 meter
list6 = [
    {'INPUT' : 'Move up by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": true, "unit": "meter" } }'}
]

# Upwards by 3.5 meters
list7 = [
    {'INPUT' : 'Move up by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards by 3.5 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 3.5, "is_upward": true, "unit": "meter" } }'}
]

# Upwards using 'for'
list8 = [
    {'INPUT' : 'Move up for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards for 7 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 7, "is_upward": true, "unit": "meter" } }'}
]

# Upwards with only speed meters per second
list9 = [
    {'INPUT' : 'Move up with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'}
]

# Upwards with only speed m/s
list10 = [
    {'INPUT' : 'Move up at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards at a speed of 2.1 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2.1, "distance": 1, "is_upward": true, "unit": "meter" } }'}
]

# Upwards with only speed simplified
list11 = [
    {'INPUT' : 'Move up at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher fat 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": true, "unit": "meter" } }'}
]

# Upwards with combined distance and speed
list12 = [
    {'INPUT' : 'Move up at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards at 3 m/s for 3 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 3, "is_upward": true, "unit": "meter" } }'}
]

# Upwards with combined distance and speed decimal
list13 = [
    {'INPUT' : 'Move up by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move in the upward direction by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'ascend by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go up by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'advance upward by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'move to a higher position by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'increase altitude by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate position by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'shift higher by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'propel upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb to an elevated position by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise towards the top with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'elevate in the upward direction by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise to an elevated position by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb up by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'climb upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift up by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift off by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'lift upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise up by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'raise upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise up by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'rise upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'},
    {'INPUT' : 'go upwards by 2.1 meters with a speed of 0.3 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 0.3, "distance": 2.1, "is_upward": true, "unit": "meter" } }'}
]

# Downwards by 1 meter
list14 = [
    {'INPUT' : 'Move down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point by 1 meter', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 1, "is_upward": false, "unit": "meter" } }'}
]

# Downwards by 4.8 meters
list15 = [
    {'INPUT' : 'down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'Move down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point by 4.8 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 4.8, "is_upward": false, "unit": "meter" } }'}
]

# Downwards using 'for'
list16 = [
    {'INPUT' : 'Move down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point for 11 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 1, "distance": 11, "is_upward": false, "unit": "meter" } }'}
]

# Downwards with only speed meters per second
list17 = [
    {'INPUT' : 'Move down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point with a speed of 2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 2, "distance": 1, "is_upward": false, "unit": "meter" } }'}
]

# Downwards with only speed m/s
list18 = [
    {'INPUT' : 'Move down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point at a speed of 13.2 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 13.2, "distance": 1, "is_upward": false, "unit": "meter" } }'}
]

# Downwards with only speed simplified
list19 = [
    {'INPUT' : 'Move down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point at 3 m/s', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3, "distance": 1, "is_upward": false, "unit": "meter" } }'}
]

# Downwards with combined distance and speed
list20 = [
    {'INPUT' : 'Move down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point at 5 m/s for 9 meters', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 5, "distance": 9, "is_upward": false, "unit": "meter" } }'}
]

# Downwards with combined distance and speed decimals
list21 = [
    {'INPUT' : 'down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'Move down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move in the downward direction by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move downwards by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop downwards by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower downwards by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall downwards by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'sink downwards by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decline by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'depress by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'plummet by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'go down by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower in the downwards direction by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall in the downwards direction by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'drop to a lower position by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'move to a lower position by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'decrease altitude by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower altitude by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'lower the position by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'descend to a lower position by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'},
    {'INPUT' : 'fall to a lower point by 2.7 meters with a speed of 3.2 meters per second', 'OUTPUT': '{ "action": "move", "params": { "linear_speed": 3.2, "distance": 2.7, "is_upward": false, "unit": "meter" } }'}
]

new_rows = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14 + list15 + list16 + list17 + list18 + list19 + list20 + list21

new_set = Dataset.from_dict({key: [item[key] for item in new_rows] for key in new_rows[0].keys()})

dataset['train'] = concatenate_datasets([dataset['train'], new_set])

last_item = dataset['train'][-1]
print(dataset['train'])

# # # # #
# End of upwards and downwards commands
#

# Save the modified dataset
dataset.save_to_disk('modified_set')
