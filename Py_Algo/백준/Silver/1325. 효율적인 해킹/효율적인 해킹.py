def bfs(start):
    global mx_cnt
    global mx_res

    visited = [False] * (N + 1)
    visited[start] = True
    queue = deque([start])
    cnt = 0

    while queue:
        vertex = queue.popleft()
        cnt += 1

        for node in trust[vertex]:
            if visited[node] == False:
                visited[node] = True
                queue.append(node)

    if mx_cnt < cnt:
        mx_cnt = cnt
        mx_res = [start]
    elif mx_cnt == cnt:
        mx_res.append(start)

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
trust = [[] for _ in range(N + 1)]
res = []

for _ in range(M):
    A, B = map(int, input().split())

    if A not in trust[B]:
        trust[B].append(A)

mx_cnt = 0
mx_res = []

for idx in range(1, N + 1):
    bfs(idx)

print(*sorted(mx_res))