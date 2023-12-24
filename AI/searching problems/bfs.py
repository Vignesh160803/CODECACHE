def bfs(graph,start,visited):
    queue = []
    queue.append(start)
    visited.append(start)
    while queue:
         u = queue.pop(0)
         for neighbor in graph[u]:
              if neighbor not in visited:
                   visited.append(neighbor)
                   queue.append(neighbor)
    
    print(visited)


graph = {
    1:[3,2],
    2:[1,5],
    3:[1,4],
    4:[3],
    5:[2]
}

bfs(graph,1,[])