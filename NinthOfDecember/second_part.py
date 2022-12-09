import numpy as np

f = open("head_movement", "r")
#f = open("example_movements_part2", "r")

lines = f.readlines()

segments = [np.array([0, 0]) for _ in range(10)]
positions = set()
direction_translation = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L':(0, -1)}

#print(numpy_euclidian_distance(tuple(np.array([0,0])), tuple(np.array([0,2]))))

def make_move(segments, direction):
    segments[0] += direction
    
    for i in range(len(segments)-1):
        if max(abs(segments[i] - segments[i+1])) > 1:
            segments[i+1] += np.clip((segments[i] - segments[i+1]), -1, 1)

for line in lines:
    direction, distance = line.split(" ")
    for step in range(int(distance)):
        translated_direction = direction_translation[direction]
        make_move(segments,translated_direction)
        positions.add(tuple(segments[-1]))
        
print(len(positions))


