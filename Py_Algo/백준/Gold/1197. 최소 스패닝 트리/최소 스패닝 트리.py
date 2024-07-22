def find(elem):
    if parent[elem] == elem:
        return elem

    parent[elem] = find(parent[elem])
    return parent[elem]

def union(elem1, elem2):
    elem1 = find(elem1)
    elem2 = find(elem2)

    if elem1 > elem2:
        parent[elem1] = elem2
    else:
        parent[elem2] = elem1

import heapq

N, E = map(int, input().split())
edges = []
parent = [child for child in range(N + 1)]
total = 0

for _ in range(E):
    n1, n2, w = map(int, input().split())
    heapq.heappush(edges, (w, n1, n2))

while edges:
    weight, start, end = heapq.heappop(edges)

    if find(start) != find(end):
        total += weight
        union(start, end)

print(total)