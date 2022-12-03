f = open("rucksacks_contents", "r")
example = open("example_contents", "r")

sum_of_priorities_of_repeated_items = 0

def split_in_half(contents):
    half = len(contents)//2
    return contents[slice(0, half)], contents[slice(half, len(contents))]

def find_duplicate_item(first_compartment_items, second_compartment_items):
    for item in first_compartment_items:
        if item in second_compartment_items:
                return(item)

def get_item_priority(item):
    
    priority = 0
    decimal_item_value = ord(item)
    
    if 96 < decimal_item_value <= 122:
        priority = decimal_item_value - 96
    elif 64 < decimal_item_value <= 90:
        priority = decimal_item_value - 38
    
    return priority

lines = f.readlines()

for line in lines:
    
    split_content = split_in_half(line)
    first_compartment = split_content[0]
    second_compartment = split_content[1]
    duplicate_item = find_duplicate_item(first_compartment, second_compartment)
    item_priority = get_item_priority(duplicate_item)
    sum_of_priorities_of_repeated_items = sum_of_priorities_of_repeated_items + item_priority
    
print(sum_of_priorities_of_repeated_items)
