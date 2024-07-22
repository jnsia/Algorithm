def dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            answer[node] += answer[next_node]


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
answer = [1] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)

for _ in range(Q):
    key = int(input())
    print(answer[key])