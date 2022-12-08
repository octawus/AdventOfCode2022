#MOVEMENT FORMAT
#move 2 from 4 to 6
import pandas as pd

def obtain_easy_to_work_with_data(file):
    colspecs = [(0, 3), (4, 7), (8, 12), (12, 15), (16, 19), (20, 23), (24, 27), (28, 31), (32, 35)]

    data = pd.read_fwf(file, dtype=str ,colspecs = colspecs, header=None, nrows=9)
    data = data.drop(labels=8)
    data = data.fillna('')
    data = data.replace('\[', '', regex=True)
    data = data.replace('\]', '', regex=True)

    return data

def execute_crate_movement(crates_state, no_of_crates, start_column, end_column):
    
    for i in range(no_of_crates):
        if crates_state[start_column]:
            crates_state[end_column].append(crates_state[start_column].pop())
    
def get_first_element_of_all_column(crates_state):
    solution = ""
    for i in range (0, 9):
        solution = solution + crates_state[i].pop()
    
    return solution

def invert_matrix(matrix):
    inverted_data_matrix = []
    
    for i in range(len(matrix)):
        inverted_data_matrix.append(matrix[i][::-1])

    inverted_data_matrix = [[ele for ele in sub if ele != ""] for sub in inverted_data_matrix]

    return inverted_data_matrix

data = obtain_easy_to_work_with_data("crates_and_movements")

data_matrix = data.to_numpy()
data_matrix = list(zip(*data_matrix))
inverted_data_matrix = invert_matrix(data_matrix)

f = open('crates_and_movements', "r")

moves = f.readlines()[10:]

for move in moves:
    move = [int(s) for s in move.split() if s.isdigit()]
    execute_crate_movement(inverted_data_matrix, int(move[0]), int(move[1]-1), int(move[2]-1))

print(get_first_element_of_all_column(inverted_data_matrix))
