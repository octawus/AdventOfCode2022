f = open("rucksacks_contents", "r")
example = open("example_contents", "r")

sum_of_groups_common_items_priorities = 0

def get_item_priority(item):
    
    priority = 0
    decimal_item_value = ord(item)
    
    if 96 < decimal_item_value <= 122:
        priority = decimal_item_value - 96
    elif 64 < decimal_item_value <= 90:
        priority = decimal_item_value - 38
    
    return priority

lines = f.readlines()
number_of_rucksacks = len(lines)
counter = 0

for group_id in range(0, number_of_rucksacks, 3):

    first_elf = lines[group_id].rstrip()
    second_elf = lines[group_id + 1].rstrip()
    third_elf = lines[group_id + 2].rstrip()
        
    common_item = ''.join(set(first_elf).intersection(second_elf).intersection(third_elf))
    
    sum_of_groups_common_items_priorities = sum_of_groups_common_items_priorities + get_item_priority(common_item)
    
print(sum_of_groups_common_items_priorities)