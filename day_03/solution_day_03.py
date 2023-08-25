file_path = './input_day_03.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()


# Initialize a variable to store the sum of the priorities
total_priority = 0

# Iterate through each line to find the common item type in both compartments for each rucksack
for line in lines_day_3:
    line = line.strip()
    # Split the items into two sets, one for each compartment
    half_length = len(line) // 2
    compartment_1 = set(line[:half_length])
    compartment_2 = set(line[half_length:])
    
    # Find the common item type
    common_items = compartment_1.intersection(compartment_2)
    
    # There should be exactly one common item type per rucksack according to the problem statement
    common_item = list(common_items)[0]
    
    # Calculate the priority of the common item type
    if 'a' <= common_item <= 'z':  # Lowercase letter
        priority = ord(common_item) - ord('a') + 1
    else:  # Uppercase letter
        priority = ord(common_item) - ord('A') + 27
    
    # Add the priority to the total sum
    total_priority += priority

total_priority
