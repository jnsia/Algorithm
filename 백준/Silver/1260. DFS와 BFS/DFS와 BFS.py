def dfs(graph, start):
    visited = set()
    stack = [start]
    route = []
    
    while stack:
        vertex = stack.pop()
        
        for item in reversed(sorted(graph[vertex])):
            if item not in visited:
                stack.append(item)
        
        if vertex not in visited:
            visited.add(vertex)
            route.append(vertex)
    
    return route

def bfs(graph, start):
    visited = set()
    queue = [start]
    route = []
    
    while queue:
        vertex = queue.pop(0)
        
        for item in sorted(graph[vertex]):
            if item not in visited:
                queue.append(item)
        
        if vertex not in visited:
            visited.add(vertex)
            route.append(vertex)
            
    return route

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

node_dict = {}

for j in range(1, N + 1):
    node_dict[j] = []

for i in range(M):
    pn, cn = map(int, input().split())
    
    node_dict[pn].append(cn)
    node_dict[cn].append(pn)
    
print(*dfs(node_dict, V))
print(*bfs(node_dict, V))