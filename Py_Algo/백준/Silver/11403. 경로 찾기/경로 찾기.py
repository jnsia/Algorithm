def bfs(start):
    queue = deque([start])
    res = [0] * N

    while queue:
        v = queue.pop()

        for u in range(N):
            if A[v][u] == 1 and res[u] == 0:
                queue.append(u)
                res[u] = 1

    print(*res)

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
res = [[0] * N for _ in range(N)]

for i in range(N):
    bfs(i)