def bfs(start):
    mn_dist = [200000000] * (N + 1)
    mn_dist[0] = 0
    mn_dist[start] = 0
    hq = [[0, start]]

    while hq:
        dist, node = heapq.heappop(hq)

        if dist > mn_dist[node]:
            continue

        for next_dist, next_node in arr[node]:
            if mn_dist[next_node] > dist + next_dist:
                mn_dist[next_node] = mn_dist[node] + next_dist
                heapq.heappush(hq, [mn_dist[next_node], next_node])

    return mn_dist

import heapq

N, E = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    arr[a].append([c, b])
    arr[b].append([c, a])

v1, v2 = map(int, input().split())

v0_mn_dist = bfs(1)
v1_mn_dist = bfs(v1)
v2_mn_dist = bfs(v2)

if v0_mn_dist[N] >= 200000000:
    print(-1)
else:
    print(min(v0_mn_dist[v1] + v1_mn_dist[v2] + v2_mn_dist[N], v0_mn_dist[v2] + v2_mn_dist[v1] + v1_mn_dist[N]))
