def dfs(graph,visited,start):
    stack = []
    stack.append(start)
    visited.append(start)

    while stack:
        u = stack.pop()
        for neighbor in graph[u]:
            if neighbor not in visited:
                dfs(graph,visited,neighbor)
    

graph = {
    1:[3,2],
    2:[1,5],
    3:[1,4],
    4:[3],
    5:[2]
}
visited = []
dfs(graph,visited,1)
print(visited)