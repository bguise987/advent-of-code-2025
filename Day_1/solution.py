import os
from pathlib import Path
import re

# We want to find how many times the dial is left at 0
# The dial starts at 50
# The dial is a circle 0 -> 99
# Each direction starts with L or R
# Run through input.txt

# Regex to split out the dial movements
dial_movement_regex = r'([RL])(\d{1,2})'
# How to use this regex:
# matches = re.match(dial_movement_regex, foo)
# tokens = list(matches.groups()) if matches else []

# Used to store and increment the number of times the dial is left at 0
zero_count = 0

