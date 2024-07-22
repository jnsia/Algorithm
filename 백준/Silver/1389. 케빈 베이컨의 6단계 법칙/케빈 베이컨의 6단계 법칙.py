def bfs(start):
    queue = [start]
    visited[start] = True
    cnt = 0
    dp = [0 for _ in range(N + 1)]

    while queue:
        for _ in range(len(queue)):
            vertex = queue.pop(0)
            dp[vertex] = cnt

            for i in range(1, N + 1):
                if graph[vertex][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)
        cnt += 1

    return sum(dp)


from pprint import pprint as print

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for m in range(M):
    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1

res_dp = [0 for _ in range(N + 1)]
res_min = N * N
res_idx = 0

for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    res_dp[i] = bfs(i)

for j in range(1, N + 1):
    if res_min > res_dp[j]:
        res_min = res_dp[j]
        res_idx = j

print(res_idx)