f = open("elf_calories", "r")

lines = f.readlines()

highest_calories = [0, 0, 0]
sum_of_calories = 0

def check_and_add(highest_calories, calories_to_add):
    for elf in highest_calories:
        if min(highest_calories) < calories_to_add:
            highest_calories[highest_calories.index(min(highest_calories))] = calories_to_add
            break

for line in lines:
    no_new_line_line = line.rstrip()
    if no_new_line_line != '':
        sum_of_calories = sum_of_calories + int(line)
    else:
        print(sum_of_calories)
        check_and_add(highest_calories, sum_of_calories)
        sum_of_calories = 0
        
        

print(f"Top 3 elfs: {highest_calories}")
print(f"The highest calories are: {sum(highest_calories)}")