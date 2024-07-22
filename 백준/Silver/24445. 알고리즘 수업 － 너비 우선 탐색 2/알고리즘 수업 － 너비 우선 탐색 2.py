def bfs(r):
    visited = [False for _ in range(N + 1)]
    result = [0 for _ in range(N + 1)]
    queue = deque([r])
    cnt = 0
    visited[r] = 1

    while queue:
        vertex = queue.popleft()
        cnt += 1
        result[vertex] = cnt

        for nv in sorted(graph[vertex], reverse=True):
            if visited[nv] == False:
                visited[nv] = True
                queue.append(nv)

    return result
        
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for n in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

result_list = bfs(R)

for k in range(1, N + 1):
    print(result_list[k])