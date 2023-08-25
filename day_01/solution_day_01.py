file_path = './input_day_01.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Initialize variables to store individual Elves' food calories and the current Elf's calories
elves_calories = []
current_elf_calories = []

# Parse the input lines to separate each Elf's food calories
for line in lines:
    line = line.strip()  # Remove any leading/trailing whitespaces
    if line:  # Check if the line is not empty
        current_elf_calories.append(int(line))
    else:
        # When we hit an empty line, we know the current Elf's list is complete
        elves_calories.append(current_elf_calories)
        current_elf_calories = []

# Append the last Elf's calories if the input doesn't end with an empty line
if current_elf_calories:
    elves_calories.append(current_elf_calories)

# Check the first few lists to verify the parsing
#elves_calories[:5]
#print(elves_calories[:5])

# Calculate the total calories for each Elf
total_calories_per_elf = [sum(elf_calories) for elf_calories in elves_calories]

# Find the Elf carrying the most calories
max_calories = max(total_calories_per_elf)
print(max_calories)

#PART 2
# Sort the total calories for each Elf in descending order
sorted_calories_per_elf = sorted(total_calories_per_elf, reverse=True)

# Take the top 3 values and sum them
top_3_calories = sum(sorted_calories_per_elf[:3])
top_3_calories
print(top_3_calories)