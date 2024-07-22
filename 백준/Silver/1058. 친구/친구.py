def func(vertex):
    visited = [False] * N
    visited[vertex] = True
    stack = []

    for next_vertex in range(N):
        if not visited[next_vertex] and graph[vertex][next_vertex]:
            visited[next_vertex] = True
            stack.append(next_vertex)
            state[vertex] += 1

    while stack:
        new_vertex = stack.pop()

        for next_vertex in range(N):
            if not visited[next_vertex] and graph[new_vertex][next_vertex]:
                visited[next_vertex] = True
                state[vertex] += 1


N = int(input())
state = [0] * N
graph = []

for _ in range(N):
    line = list(input())

    for idx in range(N):
        if line[idx] == 'Y':
            line[idx] = 1
        else:
            line[idx] = 0

    graph.append(line)

for nun in range(N):
    func(nun)

print(max(state))