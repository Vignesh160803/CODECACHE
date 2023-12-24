import math
from queue import PriorityQueue

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def a_star(start, goal, graph,coords):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = euclidean_distance(coords[start],coords[goal])

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + euclidean_distance(coords[current], coords[neighbor])
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + euclidean_distance(coords[neighbor], coords[goal])
                open_set.put((f_score[neighbor], neighbor))

    return None


# Define the graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2},
    'C': {'A': 3, 'D': 6},
    'D': {'B': 2, 'C': 6, 'E': 8},
    'E': {'D': 8}
}
# A: (0, 0) B: (2, 0) C: (1, 1) D: (3, 2) E: (4, 3)

coords = {"A":(0,0),"B":(2,0),"C":(1,1),"D":(3,2),"E":(4,3)}


# Define the start and goal nodes
start = 'A'
goal = 'E'

# Call the A* algorithm
path = a_star(start, goal, graph,coords)

# Print the path
if path:
    print("Path found:", path)
else:
    print("No path found.")
