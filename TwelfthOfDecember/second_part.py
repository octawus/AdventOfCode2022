from string import ascii_lowercase
from heapq import heappop, heappush

f = open("height_map", "r")
#f = open("example_data", "r")
heights_map = []
lines = f.read().splitlines()
for line in lines:
    heights_map.append(list(line.rstrip()))

def get_neighbors(x, y, max_x, max_y):
    #if x == 0:
    #    up = (x, y)
    #else:
    #    up = (x - 1, y)
    #if y == max_y:
    #    right = (x, y)
    #else:
    #    right = (x, y + 1)
    #if x == max_x:
    #    down = (x, y)
    #else:
    #    down  = (x + 1, y)
    #if y == 0:
    #    left = (x, y)
    #else:
    #    left = (x, y - 1)
    up = (x - 1, y) if x != 0 else (x, y)
    down = (x + 1, y) if x != max_y else (x, y)
    left = (x, y - 1) if y != 0 else (x, y)
    right = (x, y + 1) if y != max_x else (x, y)
        
    return [up, right, down, left]

def find_element(x, lst):
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                return (i, j)
    return (-1, -1)

#bfs = breadth_first_search
#https://favtutor.com/blogs/breadth-first-search-python 
#https://www.educative.io/answers/how-to-implement-a-breadth-first-search-in-python
#https://www.programiz.com/dsa/graph-bfs

#procedure BFS(G, root) is
#      let Q be a queue
#      label root as explored
#      Q.enqueue(root)
#      while Q is not empty do
#          v := Q.dequeue()
#          if v is the goal then
#              return v
#          for all edges from v to w in G.adjacentEdges(v) do
#              if w is not labeled as explored then
#                  label w as explored
#                  w.parent := v
#                  Q.enqueue(w)
def do_bfs_search(graph, root):
    heap = [(0, root)]
    q = set([root])
    max_x = len(graph[0]) - 1
    max_y = len(graph) - 1
    while heap:
        steps, (x, y) = heappop(heap)
        if graph[x][y] == 'E':
            return steps
        for neighbor in get_neighbors(x, y, max_x, max_y):
            if heights[graph[neighbor[0]][neighbor[1]]] <= heights[graph[x][y]] + 1:
                if neighbor not in q:
                    heappush(heap, (steps + 1, neighbor))
                    q.add(neighbor)
                
    return steps



    
#https://careerkarma.com/blog/python-zip/
heights = { k:v for k, v in zip(ascii_lowercase, range(len(ascii_lowercase))) }
heights['S'] = heights['a']
heights['E'] = heights['z']

posible_starts = list()
for i, line in enumerate(heights_map):
    if 'a' in line:
        posible_starts.append((i, line.index('a')))

steps = min([do_bfs_search(heights_map, start) for start in posible_starts])

print(steps)