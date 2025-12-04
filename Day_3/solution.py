from pathlib import Path

with open(Path('input.txt')) as f:
    batteries = f.read()

batteries = batteries.split()

total_output_joltage = 0

# Send in battery as string
def find_max_joltage(battery):
    max_joltage = 0
    for x in range(len(battery)):
        for y in range(x, len(battery)):
            # Combine strings, then convert to int
            joltage = int(x + y)
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage

# Iterate through batteries
for battery in batteries:
    # Find maximum joltage for given battery
    max_joltage = find_max_joltage(battery)
    # Add this joltage to total_output_joltage
    total_output_joltage += max_joltage


print(f'Inspected all battery banks...')
print(f'Total output joltage: {total_output_joltage}')
