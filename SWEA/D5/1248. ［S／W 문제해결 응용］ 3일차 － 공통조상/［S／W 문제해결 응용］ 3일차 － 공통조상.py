def dfs(graph, start):
    visited = set()
    stack = [start]
    route = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
            route.append(vertex)
    
    return route

T = int(input())

for t in range(1, T + 1):
    V, E, N, M = map(int, input().split())
    
    reverse_dictionary = {}
    dictionary = {}
    
    for i in range(1, V + 1):
        reverse_dictionary[i] = []
        dictionary[i] = []
        
    kv = list(map(int, input().split()))
    
    for j in range(0, E * 2, 2):
        reverse_dictionary[kv[j+1]].append(kv[j])
        
    # print(reverse_dictionary)
    
    N_list = dfs(reverse_dictionary, N)
    M_list = dfs(reverse_dictionary, M)
    
    # print('N:', N_list)
    # print('M:', M_list)
    
    c = 0
    
    break_button = False
    
    for n in N_list:
        for m in M_list:
            if n == m:
                c = n
                break_button = True
                break
            
        if break_button:
            break
            
    for k in range(0, E * 2, 2):
        dictionary[kv[k]].append(kv[k+1])
    
    print(f'#{t}', end=" ")    
    print(c, end=" ")    
    print(len(dfs(dictionary, c)))