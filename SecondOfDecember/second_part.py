# X = Lose
# Y = Draw
# Z = Win

# A = Rock
# B = Paper
# C = Scissors

f = open("shady_elf_strategy", "r")

lines = f.readlines()

choices = {
    
    "AX": 3,
    "AY": 1,
    "AZ": 2, 
    "BX": 1,
    "BY": 2,
    "BZ": 3,
    "CX": 2,
    "CY": 3,
    "CZ": 1

}

def get_score(elf_choice, how_to_end):
    score = 0
    if how_to_end == "Y":
        score = 3
    elif how_to_end == "Z":
        score = 6
        
    my_choice = elf_choice + how_to_end
    score_of_my_choice = choices[my_choice]
    
    return score + score_of_my_choice

total_score = 0
for line in lines:
    no_new_line_line = line.rstrip()
    options = no_new_line_line.split(" ")
    
    score_for_round = get_score(options[0], options[1])
    total_score = total_score + score_for_round    

print(total_score)