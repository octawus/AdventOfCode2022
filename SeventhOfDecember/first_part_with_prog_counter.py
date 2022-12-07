#f = open("executed_commands_and_output", "r")
f = open("small_example", "r")

commands_and_output = f.readlines()
current_path = ""
file_system = {}
line_counter = 0

def decide_if_command_or_output(line):
    if line[0] == "$":
        return "command"
    else:
        return "output"
    
def parse_command(line):
    elements = line.split(" ")
    return elements[1:]

def do_command_logic(command_elements):
    pass

def change_directory(parameter):
    global current_path
    global line_counter
    if parameter == "/":
        current_path = "/"
    elif parameter == "..":
        current_path = current_path.rsplit("/", 1)[0]
    else:
        if current_path == "/":
            current_path = current_path + f"{parameter}"
        else:
            current_path = current_path + f"/{parameter}"
    
    line_counter += 1
    
            
def list_on_steroids():
    global file_system
    global line_counter
    print("llego aqui")
    print(line_counter)
    while commands_and_output[line_counter][0] != "$":
        print(commands_and_output[line_counter])
        line_counter += 1
        
def construct_baby_filesystem():
    global line_counter
    line = commands_and_output[line_counter].rstrip()
    
    while line != "":
        print(line)
        if decide_if_command_or_output(line) == "command":
            command_elements = parse_command(line)
            if command_elements[0] == "ls":
                list_on_steroids()
            elif command_elements[0] == "cd":
                change_directory(command_elements[1])
                print(command_elements)
                print(current_path)
        #else:
        #    print(command_elements)
        #    print(line)
        line = commands_and_output[line_counter].rstrip()
            


construct_baby_filesystem()