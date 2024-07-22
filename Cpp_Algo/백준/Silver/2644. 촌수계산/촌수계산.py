N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

answer = 0
visited = [0] * (N + 1)

queue = []
queue.append(a)
visited[a] = 1

while queue:
    vertex = queue.pop(0)

    for next_vertex in graph[vertex]:
        if visited[next_vertex] == 0:
            visited[next_vertex] = visited[vertex] + 1
            queue.append(next_vertex)

print(visited[b] - visited[a])