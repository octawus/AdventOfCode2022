import numpy as np

# https://stackoverflow.com/a/18566637 (for left slicing, 
# and bassically master class on slicing in python)
# https://stackoverflow.com/q/15627312 (Why None in stop of np.array)

forest = np.genfromtxt("treemap", delimiter=1, dtype=int, encoding=None)
#forest = np.genfromtxt("example", delimiter=1, dtype=int, encoding=None)

def get_perimeter_of_forest(forest):
    dimensions = forest.shape
    return ((dimensions[0]-2) * 2 + (dimensions[1]-2) * 2) + 4
    
def get_element_to_the_right(x, y):
    return list(forest[y, x:])

def get_elements_to_the_left(x, y):
    return list(forest[y, x::-1])

def get_element_to_the_top(x, y):
    return list(forest[y:None:-1, x])

def get_elements_to_the_bottom(x, y):
    return list(forest[y:None:1, x])

def check_if_tallest_tree(list_of_trees):
    if list_of_trees[0] <= max(list_of_trees[1:]):
        return False
    else:
        return True

def get_number_of_trees_until_first_equal(list_of_trees):
    print(list_of_trees[0])
    print(list_of_trees)
    visible_trees = 0
    for tree in list_of_trees[1:]:
        if list_of_trees[0] > tree:
            visible_trees += 1
        elif list_of_trees[0] <= tree:
            visible_trees += 1
            break
    print(visible_trees)
    return visible_trees     
    
def obtain_specific_tree_scenic_score(x, y):
    print(f"For x:{x} y:{y}")
    scenic_score = get_number_of_trees_until_first_equal(get_element_to_the_right(x, y))*get_number_of_trees_until_first_equal(get_elements_to_the_left(x, y))*get_number_of_trees_until_first_equal(get_element_to_the_top(x, y))*get_number_of_trees_until_first_equal(get_elements_to_the_bottom(x, y))

    print(f"Scenic score: {scenic_score}")
    return scenic_score

def get_most_derirable_tree(matrix):
    dimensions_x_y = matrix.shape
    score_of_most_desirable = 0
    for i in range (0, dimensions_x_y[0]):
        for j in range (0, dimensions_x_y[1]):
            current_score = obtain_specific_tree_scenic_score(i, j)
            if score_of_most_desirable < current_score:
                score_of_most_desirable = current_score
    return score_of_most_desirable

most_desirable_tree_score = get_most_derirable_tree(forest)
print(f"Most desirable tree has {get_most_derirable_tree(forest)} score")