from queue import PriorityQueue

def best_first_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        cost, node = queue.get()

        if node == goal:
            return True

        visited.add(node)

        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited:
                queue.put((neighbor_cost, neighbor))

    return False

# Example usage
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 4), ('E', 6)],
    'D': [('F', 1)],
    'E': [('F', 8)],
    'F': []
}

start_node = 'A'
goal_node = 'F'

result = best_first_search(graph, start_node, goal_node)
print(result)
