def DLS(graph,start,goal,max_depth):
    if start==goal:
        return True
    if max_depth<=0:
        return False
    
    for neighbor in graph[start]:
        if DLS(graph,neighbor,goal,max_depth-1):
            return True
    
    return False


def IDDFS(graph,start,goal,max_depth):
    for i in range(1,max_depth+1):
        if DLS(graph,start,goal,i):
            return True
    
    return False



graph = {
    1:[3,2],
    2:[3],
    3:[2,4],
    4:[5],
    5:[4]
}

print(IDDFS(graph,1,5,2))
print(IDDFS(graph,1,5,3))