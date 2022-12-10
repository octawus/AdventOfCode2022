f = open("input_ops", "r")

lines = f.readlines()

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
      
        if instruction == "noop":
            cycle_counter += 1
            line_counter += 1
            increment = False
        if instruction == "addx":
            cycle_counter += 1
            if not first_iteration:
                print(f"Incrementing {register} by {parameter} on line {line_counter + 1} on cycle {cycle_counter} and obtaining:")
                increment = True
                print(f"{register}")
                line_counter += 1
                read_next_instruction = True
                first_iteration = True
            else:
                increment = False
                first_iteration = False
                read_next_instruction = False
        
        if cycle_counter == 20 or (cycle_counter - 20)%40 == 0:
            print(f"The register has {register}, during {cycle_counter} cycle, instruction number:{line_counter}, instruction {instruction}, parameter {parameter}")
            signal_strenght += register * cycle_counter
        
        if increment == True:
            register += int(parameter)
            
    return signal_strenght

signal_strenght = start_execution()
print(signal_strenght)
            
    
