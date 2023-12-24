from collections import deque

def bidirectional_search(graph, start, goal):
    # Create two sets to track visited nodes from both directions
    visited_start = set()
    visited_goal = set()

    # Create two queues to perform BFS from both directions
    queue_start = deque([(start, [start])])
    queue_goal = deque([(goal, [goal])])

    while queue_start and queue_goal:
        # Perform BFS from the start direction
        node_start, path_start = queue_start.popleft()
        visited_start.add(node_start)

        if node_start in visited_goal:
            # If the node is visited from both directions, return the combined path
            path_goal = []  # Initialize path_goal with an empty list
            return path_start + path_goal[::-1]

        for neighbor in graph[node_start]:
            if neighbor not in visited_start:
                queue_start.append((neighbor, path_start + [neighbor]))

        # Perform BFS from the goal direction
        node_goal, path_goal = queue_goal.popleft()
        visited_goal.add(node_goal)

        if node_goal in visited_start:
            # If the node is visited from both directions, return the combined path
            return path_start + path_goal[::-1]

        for neighbor in graph[node_goal]:
            if neighbor not in visited_goal:
                queue_goal.append((neighbor, path_goal + [neighbor]))

    # If no path is found, return None
    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'G'],
    'F': ['D', 'H'],
    'G': ['E', 'I'],
    'H': ['F', 'J'],
    'I': ['G'],
    'J': ['H']
}

start_node = 'A'
goal_node = 'I'

path = bidirectional_search(graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found.")
