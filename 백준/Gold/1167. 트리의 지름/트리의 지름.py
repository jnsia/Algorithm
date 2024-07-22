def bfs(node):
    dist = [-1] * (N + 1)
    dist[node] = 0
    queue = [node]

    while queue:
        vertex = queue.pop(0)

        for next_node, weight in adj[vertex]:
            if dist[next_node] == -1:
                dist[next_node] = dist[vertex] + weight
                queue.append(next_node)

    mx_dist = 0
    mx_node = 0

    for num in range(1, N + 1):
        if mx_dist < dist[num]:
            mx_dist = dist[num]
            mx_node = num

    return mx_node, mx_dist


N = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N):
    arr = list(map(int, input().split()))

    parent = arr[0]

    for idx in range(1, len(arr), 2):
        if arr[idx] == -1:
            break
        else:
            adj[parent].append([arr[idx], arr[idx + 1]])

mx_vertex, mx_distance = bfs(1)
mx_vertex, mx_diameter = bfs(mx_vertex)

print(mx_diameter)