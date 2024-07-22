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


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    parent = [_ for _ in range(V + 1)]
    vertex_set = [-1] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        union(u, v)

    queue = []

    for i in range(1, V + 1):
        if parent[i] == i:
            queue.append(i)
            vertex_set[i] = 0

    is_bipartite = True

    while queue:
        vertex = queue.pop(0)

        if not is_bipartite:
            break

        for next_vertex in graph[vertex]:
            if vertex_set[next_vertex] == -1:
                vertex_set[next_vertex] = vertex_set[vertex]^1
                queue.append(next_vertex)
                continue

            if vertex_set[vertex] == vertex_set[next_vertex]:
                is_bipartite = False
                break

    if is_bipartite:
        print('YES')
    else:
        print('NO')