import re

f = open("cleaning_instructions", "r")
#f = open("small_personal_example", "r")

lines = f.readlines()

no_of_overlapings = 0

def asert_if_overlaped(first_elf_set, second_elf_set):
    
    if bool(first_elf_set & second_elf_set):
        return True
    else:
        return False  

#print(asert_if_contained(set(range(1,4)), set(range(4,8))))
for line in lines:
    
    elf_asignements = re.split(r'[,-]', line.rstrip())
    
    first_elf_set_of_sections = set(range(int(elf_asignements[0]), int(elf_asignements[1])+1))
    second_elf_set_of_sections = set(range(int(elf_asignements[2]), int(elf_asignements[3])+1))
    
    if asert_if_overlaped(first_elf_set_of_sections, second_elf_set_of_sections):
        print(f"In this asignement there is overlaping {elf_asignements}")
        no_of_overlapings = no_of_overlapings + 1
    else:
        print(f"There is no overlaping {elf_asignements}")


print(no_of_overlapings)