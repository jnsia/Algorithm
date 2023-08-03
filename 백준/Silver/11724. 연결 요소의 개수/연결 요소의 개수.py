def bfs(graph, start):
    # visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        # visited.add(vertex)

        for j in graph[vertex]:
            # if j not in visited:
            if dp[j] == 0:
                queue.append(j)
                dp[j] = 1

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

cc_dict = dict()

for num in range(1, N + 1):
    cc_dict.setdefault(num, [])

for _ in range(M):
    n, m = map(int, input().split())

    cc_dict[n].append(m)
    cc_dict[m].append(n)

dp = [0] * (N + 1)
res = 0

for i in range(1, N + 1):
    if dp[i] == 0:
        bfs(cc_dict, i)
        res += 1

print(res)