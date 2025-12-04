from pathlib import Path

# Check the database
# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
# Example: 11-22 is set inclusive, 11 and 22 are both invalid (repeated digits)
# Find all invalid IDs in the given ranges
# Invalid IDs have patterns repeated AT LEAST TWICE (example: 55, 6464, 123123, 111)
# There are no leading 0s

# Answer: Sum of ALL of the invalid IDs

invalid_id_sum = 0

# How do we identify a pattern in the ID?
# Convert to string
# Invalid IDs have pattern repeated AT LEAST TWICE
# Divide string in half, compare first and second half

# Helper function!
# Input: sequence, whole string
# Output: Count of how many times that sequence appears in the string
# Maybe we didn't need this helper function...oh well
def find_sequence_count(sequence, search_string):
    return search_string.count(sequence)

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

        # Iterate through possible string sequences (len 1, 2, 3, 4...)
        for sequence_len in range(1, len(test_string)):
            sequence = test_string[0:sequence_len]
            # Pass sequence and search string into find_sequence_count
            sequence_count = find_sequence_count(sequence, test_string)
            # If sequence count >= 2, add to invalid_id_sum and move onto next database ID (break out of for loop)
            if sequence_count >= 2:
                invalid_id_sum += index
                break

     



print(f'Searched through DB entries...')
print(f'Invalid ID sum is: {invalid_id_sum}')
