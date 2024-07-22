def dfs(node):
    visited[node] = True
    dp[node][1] = 1

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node][0], dp[next_node][1])

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(min(dp[1]))
