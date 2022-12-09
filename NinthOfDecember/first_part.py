import numpy as np

f = open("head_movement", "r")
#f = open("example_movements", "r")

lines = f.readlines()

head_and_tail = [np.array([0,0]), np.array([0,0])]
positions = set()
direction_translation = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L':(0, -1)}

def numpy_euclidian_distance(point_1, point_2):
    array_1, array_2 = np.array(point_1), np.array(point_2)
    squared_distance = np.sum(np.square(array_1 - array_2))
    distance = np.sqrt(squared_distance)
    return int(distance)

#print(numpy_euclidian_distance(tuple(np.array([0,0])), tuple(np.array([0,2]))))

def make_move(head_and_tail, direction):
    head_and_tail[0] += direction
    auxiliary_coordinate = np.array([0,0])
    
    if numpy_euclidian_distance(tuple(head_and_tail[0]), tuple(head_and_tail[1])) > 1:
        #if same row or same column: tail follows head
        if head_and_tail[0][0] == head_and_tail[1][0] or head_and_tail[0][1] == head_and_tail[1][1]:
            head_and_tail[1] += direction
        #no same row or column (head diagonal to tail):
        else:
            auxiliary_coordinate = np.copy(head_and_tail[1])
            auxiliary_coordinate += direction
            auxiliary_coordinate += direction
            auxiliary_coordinate = head_and_tail[0] - auxiliary_coordinate
            #print(auxiliary_coordinate) 
            head_and_tail[1] += direction
            head_and_tail[1] += auxiliary_coordinate
            
    #print(head_and_tail)

for line in lines:
    direction, distance = line.split(" ")
    for step in range(int(distance)):
        translated_direction = direction_translation[direction]
        make_move(head_and_tail,translated_direction)
        positions.add(tuple(head_and_tail[1]))
        
print(len(positions))


