import os
from pathlib import Path
import re

# We want to find how many times the dial is left at 0
# The dial starts at 50
# The dial is a circle 0 -> 99
# Each direction starts with L or R
# Run through input.txt

# Regex to split out the dial movements
dial_movement_regex = r'([RL])(\d{1,5})'
# How to use this regex:
# matches = re.match(dial_movement_regex, foo)
# tokens = list(matches.groups()) if matches else []

LEFT_DIRECTION = 'L'
RIGHT_DIRECTION = 'R'

# Used to store and increment the number of times the dial is left at 0
zero_count = 0
# Store start position
start_position = 50

# Track the current position
current_position = start_position

with open(Path('input.txt'), encoding="utf-8") as f:
    dial_inputs = f.read()

# Split on newline chars to get list of the inputs
dial_inputs = dial_inputs.split()

# Iterate through dial_inputs to manipulate the dial and count times it is left at 0
for movement in dial_inputs:
    matches = re.match(dial_movement_regex, movement)
    tokens = list(matches.groups()) if matches else []

    direction = tokens[0]
    movement_count = int(tokens[1])

    # If R, add
    # If L, subtract

    if direction is LEFT_DIRECTION:
        current_position -= movement_count
    elif direction is RIGHT_DIRECTION:
        current_position += movement_count

    current_position %= 100

    if current_position == 0:
        zero_count += 1

print(f'Successfully ran through all dial inputs')
print(f'Dial was left at 0 this many times: {zero_count}')
