import numpy as np

# https://stackoverflow.com/a/18566637 (for left slicing, 
# and bassically master class on slicing in python)
# https://stackoverflow.com/q/15627312 (Why None in stop of np.array)

#forest = np.genfromtxt("treemap", delimiter=1, dtype=int, encoding=None)
forest = np.genfromtxt("example", delimiter=1, dtype=int, encoding=None)

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
            
def assert_if_specific_tree_is_visible(x, y):
    if check_if_tallest_tree(get_element_to_the_right(x, y)) or \
       check_if_tallest_tree(get_elements_to_the_left(x, y)) or \
       check_if_tallest_tree(get_element_to_the_top(x, y))   or \
       check_if_tallest_tree(get_elements_to_the_bottom(x, y)): 
        return True
    else:
        return False

def get_number_of_visible_trees_inside_inner_matrix(matrix):
    dimensions_x_y = matrix.shape
    no_of_visible_trees = 0
    for i in range (1, dimensions_x_y[0]-1):
        for j in range (1, dimensions_x_y[1]-1):
            if assert_if_specific_tree_is_visible(i, j):
                no_of_visible_trees += 1
    return no_of_visible_trees

border = get_perimeter_of_forest(forest)
internal_visible_trees = get_number_of_visible_trees_inside_inner_matrix(forest)
total_visible_trees = border + internal_visible_trees
print(f"Total visible trees: {total_visible_trees}")