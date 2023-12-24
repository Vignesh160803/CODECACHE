import heapq

class Node:

    def __init__(self,state,cost,parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent
    
    def __lt__(self,other):
        return self.cost < other.cost
    

def path_construct(node):
    path = []
    while node:
        path.insert(0,node.state)
        node = node.parent
    
    return path


def ucs(graph,start,goal):
    
    queue = []
    visited = []

    start_node = Node(start,0)
    heapq.heappush(queue,start_node)

    while queue:
        current = heapq.heappop(queue)

        if current.state == goal:
            return path_construct(current)
        if current.state not in visited:
            visited.append(current.state)
        

        for neighbor,cost in graph[current.state]:
            if neighbor not in visited:
                new_cost = current.cost+cost
                heapq.heappush(queue,Node(neighbor,cost,current))
        
    return None


example_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
goal_node = 'D'

result = ucs(example_graph, start_node, goal_node)

if result:
    print(f"Path from {start_node} to {goal_node}: {result}")
else:
    print(f"No path found from {start_node} to {goal_node}")