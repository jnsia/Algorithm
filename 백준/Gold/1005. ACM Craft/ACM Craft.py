from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    max_times = [-1] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    W = int(input())

    queue = deque()

    for i in range(1, N + 1):
        if not in_degree[i]:
            queue.append(i)
            max_times[i] = D[i - 1]

    while queue:
        vertex = queue.popleft()

        for next_vertex in graph[vertex]:
            if in_degree[next_vertex] == 1:
                queue.append(next_vertex)

            max_times[next_vertex] = max(max_times[next_vertex], D[next_vertex - 1] + max_times[vertex])
            in_degree[next_vertex] -= 1

    print(max_times[W])