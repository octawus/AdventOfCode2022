f = open("elf_calories", "r")

lines = f.readlines()

highest_calories = 0
sum_of_calories = 0

for line in lines:
    no_new_line_line = line.rstrip()
    if no_new_line_line != '':
        sum_of_calories = sum_of_calories + int(line)
    else:
        print(sum_of_calories)
        if highest_calories < sum_of_calories:
            highest_calories = sum_of_calories
        sum_of_calories = 0
        
print(f"The highest calories are: {highest_calories}")
    


