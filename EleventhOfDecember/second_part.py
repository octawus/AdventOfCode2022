import re
import math

f = open("monkeys_logic", "r").read()
#f = open("example_data", "r").read()

monke_list=[]

class Monke:
    def __init__(self, number, items, divide_by, operation, divide_true, divide_false):
        self.name = "monke"+number
        self.items = items
        self.divide_by = divide_by
        self.operation = operation
        self.divide_true = divide_true
        self.divide_false = divide_false
    
    def show_monke(self):
        #Because monke wrecks havok but its polite
        print(f"I'am: {self.name}")
        print(f"I have this stuff: {self.items}")
        print(f"I will do the following operation: {self.operation}")
        print(f"I will check if element is divisible by {self.divide_by}")
        print(f"If divisible I will throw the object to monke{divide_true}")
        print(f"If not divisible I will throw the object to monke{divide_false}")
        print("\n")

#I first separate monkes from input
#Split by ('\n\n') to split into lists of monke 
#information due to monkes having empty line inbetween
monkes_info = f.split('\n\n')

for monke in monkes_info:
    monke_lines=monke.split('\n')
    monke_no = re.findall(r'\d+', monke_lines[0])[0]
    monke_items = re.findall(r'\d+', monke_lines[1])
    operation = monke_lines[2].split(" = ")[-1]
    divide_by = int(re.findall(r'\d+', monke_lines[3])[0])
    divide_true = int(re.findall(r'\d+', monke_lines[4])[0])
    divide_false = int(re.findall(r'\d+', monke_lines[5])[0])
    monke_list.append(Monke(monke_no, monke_items, divide_by, operation, divide_true, divide_false))

monke_stuff_done = [0 for monke in monke_list]

for monke in monke_list:
    monke.show_monke()

big_gcm=1
for monke in monke_list:
    big_gcm *= monke.divide_by 
    
for round in range(10000):
    #print(f"Round: {round}")
    for i in range(len(monke_list)):
        for item in monke_list[i].items:
            monke_stuff_done[i] += 1
            old = int(item)
            new_worry = eval(monke_list[i].operation)
            new_worry %= big_gcm
            if (new_worry % monke_list[i].divide_by) == 0:
                monke_to_pass_to = monke_list[i].divide_true
            else:
                monke_to_pass_to = monke_list[i].divide_false
            monke_list[monke_to_pass_to].items.append(new_worry)
        monke_list[i].items.clear()

#print(monke_stuff_done)
monke_stuff_done.sort(reverse = True)
result = monke_stuff_done[0] * monke_stuff_done[1]
print(result)
