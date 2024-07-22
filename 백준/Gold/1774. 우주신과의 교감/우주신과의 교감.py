def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


import heapq

MAX = 2 ** 31

N, M = map(int, input().split())

parent = [_ for _ in range(N + 1)]
rank = [0] * (N + 1)
coord = [(0, 0)]
edges = []

answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x, y))

for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i != j:
            dist = ((coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2) ** 0.5
            heapq.heappush(edges, (dist, i, j))

for _ in range(M):
    start, end = map(int, input().split())
    union(start, end)

while edges:
    dist, start, end = heapq.heappop(edges)

    if find(start) != find(end):
        union(start, end)
        answer += dist

print(format(answer, ".2f"))