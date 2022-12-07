import json

f = open("executed_commands_and_output", "r")
#f = open("small_example", "r")

commands_and_output = f.readlines()
current_path = ""
file_system = {}
line_counter = 0

list_of_sums = []


def recursive_sum(n):
    current_sum = 0
    file_sum = 0
    for key in n:
        if not isinstance(n[key], dict):
            file_sum = file_sum + n[key]
            current_sum = current_sum + n[key]
        else:
            partial_sum = recursive_sum(n[key])
            print(f"Sum of elements of {key} is {partial_sum}")
            list_of_sums.append(partial_sum)
            current_sum = current_sum + partial_sum    
    return current_sum

def decide_if_command_or_output(line):
    if line[0] == "$":
        return "command"
    else:
        return "output"
    
def parse_command(line):
    elements = line.split(" ")
    return elements[1:]

def parse_output(line):
    elements = line.split(" ")
    return elements

def nest_get(dic, keys):
    result = dic
    for k in keys:
        result = result[k]
    return result

def add_value(d, path, value):
    curr = d
    for key in path:
        if key not in curr:
            curr[key] = {}
        curr = curr[key]
    k, v = value
    curr[k] = v

    return d

def change_directory(parameter):
    global current_path
    if parameter == "/":
        current_path = "/"
    elif parameter == "..":
        current_path = current_path.rsplit("/", 1)[0]
    else:
        if current_path == "/":
            current_path = current_path + f"{parameter}"
        else:
            current_path = current_path + f"/{parameter}"
            
def add_elements_to_filesystem(line):
    global file_system
    global current_path
    if current_path == "/":
        list_path = []
    else:
        list_path = current_path.split("/")
        list_path.remove("")
    elements = parse_output(line)
    if elements[0] == "dir":
        pass
        #add_value(file_system, list_path, (elements[1]))
    else:
        add_value(file_system, list_path, (elements[1], int(elements[0])))
     
def construct_baby_filesystem():
    for line_counter in range(len(commands_and_output)):
        line = commands_and_output[line_counter].rstrip()
        if decide_if_command_or_output(line) == "command":
            command_elements = parse_command(line)
            if command_elements[0] == "ls":
                pass
            elif command_elements[0] == "cd":
                change_directory(command_elements[1])
                #print(command_elements)
                #print(current_path)
        else:
            add_elements_to_filesystem(line)
            #print(line)
            
    line_counter += 1


construct_baby_filesystem()
print(json.dumps(file_system, indent=4))

with open('filesystem', 'w') as f:
    f.write(json.dumps(file_system, indent=4))
    
f.close()

summed_filesystem = recursive_sum(file_system)
print(list_of_sums)

total_sum = 0
for item in list_of_sums:
    if item < 100000:
        total_sum += item
        
print(f"Total sum for elementes lower than 100000 is: {total_sum}") 