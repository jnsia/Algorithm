def dfs(graph, start):
    visited = set()
    stack = [start]
    route = set()
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
            route.add(vertex)
    
    return route

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    people = [person for person in range(1, N + 1)]
    
    graph = {}
    
    for p in people:
        graph[p] = []
        
    for i in range(M):
        k, v = map(int, input().split())
        graph[k].append(v)
        graph[v].append(k)
        
    result = []
    new_result = []
        
    for j in people:
        result.append(dfs(graph, j))
        
    for k in result:
        if k not in new_result:
            new_result.append(k)
            
    print(f'#{t}', len(new_result))