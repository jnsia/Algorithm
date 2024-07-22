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

N = int(input())

parent = [_ for _ in range(N)]
coord = []
edges = []

answer = 0

for _ in range(N):
    x, y = map(float, input().split())
    coord.append((x, y))

for i in range(N):
    for j in range(i, N):
        if i != j:
            dist = ((coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2) ** 0.5
            heapq.heappush(edges, (dist, i, j))

while edges:
    dist, start, end = heapq.heappop(edges)

    if find(start) != find(end):
        union(start, end)
        answer += dist

print(format(answer, ".2f"))