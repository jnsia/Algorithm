def dfs(r):
    global cnt
    route[r] = cnt
    arr[r].sort()

    for g in arr[r]:
        if route[g] == 0:
            cnt += 1
            dfs(g)

import sys
sys.setrecursionlimit(150000)

N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]
route = [0] * (N + 1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

dfs(R)

for num in range(1, N + 1):
    print(route[num])
