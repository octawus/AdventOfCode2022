import numpy as np

f = open("input_ops", "r")

lines = f.readlines()

w, h = 40, 6
screen = [["." for x in range(w)] for y in range(h)] 


def start_execution():
    cycle_counter = 0
    line_counter = 0
    read_next_instruction = True
    first_iteration = True
    register = 1
    stop = False
    increment = False

    signal_strenght = 0
    while not stop:
        if read_next_instruction:
            try:
                instruction, parameter = lines[line_counter].rstrip().split(" ")
            except ValueError:
                instruction = lines[line_counter].rstrip()
            except IndexError:
                stop = True
            
        line = cycle_counter//40
        if (register - 1) <= cycle_counter%40 <= (register + 1):
            screen[line][cycle_counter%40] = "#"    
            
        if instruction == "noop":
            cycle_counter += 1
            line_counter += 1
            increment = False
        if instruction == "addx":
            cycle_counter += 1
            if not first_iteration:
                #print(f"Incrementing {register} by {parameter} on line {line_counter + 1} on cycle {cycle_counter} and obtaining:")
                increment = True
                #print(f"{register}")
                line_counter += 1
                read_next_instruction = True
                first_iteration = True
            else:
                increment = False
                first_iteration = False
                read_next_instruction = False
        
        if increment == True:
            register += int(parameter)
            
    return signal_strenght

signal_strenght = start_execution()
#print(signal_strenght)

with open('output', 'w') as output:
    for line in screen:
        string = ' '.join(line)
        output.write(string+"\n")
        print(string)
output.close()

            
    
