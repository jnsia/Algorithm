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
while True:
    M, N = map(int, input().split())

    if M == N == 0:
        break

    parent = [_ for _ in range(M)]
    edges = []
    answer = 0

    for _ in range(N):
        x, y, z = map(int, input().split())
        answer += z
        heapq.heappush(edges, (z, x, y))

    while edges:
        dist, start, end = heapq.heappop(edges)

        if find(start) != find(end):
            union(start, end)
            answer -= dist

    print(answer)