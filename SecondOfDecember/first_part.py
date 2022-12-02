# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

X = A = 1 # Rock
Y = B = 2 # Paper
Z = C = 3 # Scissors

f = open("shady_elf_strategy", "r")

lines = f.readlines()

def return_selection_score(selection):
    if selection == "X":
        return 1
    elif selection == "Y":
        return 2
    else:
        return 3
    
def check_if_draw(elf_choice, my_choice):
    if elf_choice == "A":
        elf_choice = "X"
    elif elf_choice == "B":
        elf_choice = "Y"
    else:
        elf_choice ="Z"

    if elf_choice == my_choice:
        return True
    else:
        return False
    
def play(elf_choice, my_choice):
    if check_if_draw(elf_choice, my_choice):
        return 3 + return_selection_score(my_choice)
    elif my_choice == "X":
        if elf_choice == "C":
            return 6 + return_selection_score(my_choice)
        else:
            return return_selection_score(my_choice)
    elif my_choice == "Y":
        if elf_choice == "A":
            return 6 + return_selection_score(my_choice)
        else:
            return return_selection_score(my_choice)
    elif my_choice == "Z":
        if elf_choice == "B":
            return 6 + return_selection_score(my_choice)
        else:
            return return_selection_score(my_choice)


total_score = 0
for line in lines:
    no_new_line_line = line.rstrip()
    options = no_new_line_line.split(" ")

    score_for_round = play(options[0], options[1])
    print(f"Elf choice: {options[0]}, my choice: {options[1]}, score {score_for_round}")
    total_score = total_score + score_for_round    
        
        
print(f"Total score: {total_score}")