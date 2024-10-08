import heapq

def find(x):
    if parent[x] == x:
        return x

    return find(parent[x])


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


V, E = map(int, input().split())

parent = [i for i in range(V + 1)]
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    # edges.append((c, a, b))
    heapq.heappush(edges, (c, a, b))

answer = 0
connect_count = 0
edges.sort(key=lambda x: x[0])

while edges:
    weight, start, end = heapq.heappop(edges)

    if find(start) == find(end): continue

    union(start, end)
    answer += weight
    connect_count += 1

    if connect_count == V - 1: break

print(answer)