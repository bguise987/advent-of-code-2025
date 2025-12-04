from pathlib import Path

# Check the database
# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
# Example: 11-22 is set inclusive, 11 and 22 are both invalid (repeated digits)
# Find all invalid IDs in the given ranges
# Invalid IDs have patterns repeated AT LEAST TWICE (example: 55, 6464, 123123, 111)
# There are no leading 0s

# Answer: Sum of ALL of the invalid IDs

invalid_id_sum = 0

# TODO: How do we identify a pattern in the ID?
# Convert to string
# Invalid IDs have pattern repeated EXACTLY TWICE
# Divide string in half, compare first and second half

# Open the input file
with open(Path('input.txt')) as f:
    db_ranges = f.read()

# Split the ranges out of the full list
db_ranges = db_ranges.split(',')

for search_range in db_ranges:
    # Get the first and last index to iterate through
    first_index, last_index = search_range.split('-')
    # Convert these indices to ints
    first_index = int(first_index)
    last_index = int(last_index)
    
    # +1 to last_index since they're given to us inclusive, and range()'s second arg is exclusive
    for index in range(first_index, last_index + 1):
        # Convert the number to a string
        test_string = str(index)

        str_len = len(test_string)

        # If the string can't be divided evenly in half, move on
        if str_len % 2 != 0:
            continue

        half_str = int(str_len / 2)
        # Divide the string in half
        first_half = test_string[0:half_str]
        second_half = test_string[half_str:]

        # If the halves match, add it to our total
        if first_half == second_half:
            invalid_id_sum += index


print(f'Searched through DB entries...')
print(f'Invalid ID sum is: {invalid_id_sum}')
