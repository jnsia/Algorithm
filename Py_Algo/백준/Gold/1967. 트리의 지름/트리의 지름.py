def dfs(n, w_sum):
    if len(adj[n]) > 0:
        for cn, cw in adj[n]:
            if dist[cn] == -1:
                dist[cn] = w_sum + cw
                dfs(cn, w_sum + cw)


import sys
sys.setrecursionlimit(10000)

N = int(input())
adj = [[] for _ in range(N + 1)]
dist = [-1] * (N + 1)
mx_dist = 0
mx_dist_node = 0

for _ in range(N - 1):
    p, c, w = map(int, input().split())

    adj[p].append([c, w])
    adj[c].append([p, w])

dist[1] = 0
dfs(1, 0)

for idx in range(1, N + 1):
    if mx_dist < dist[idx]:
        mx_dist = dist[idx]
        mx_dist_node = idx


dist = [-1] * (N + 1)
dist[mx_dist_node] = 0

dfs(mx_dist_node, 0)

mx_diameter = 0

for idx in range(1, N + 1):
    if mx_diameter < dist[idx]:
        mx_diameter = dist[idx]

print(mx_diameter)