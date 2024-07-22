import heapq

def bfs(start):
    mn_dist = [MAX] * (N + 1)
    mn_dist[start] = 0
    queue = [(0, start)]

    while queue:
        dist, vertex = heapq.heappop(queue)

        if dist > mn_dist[vertex]:
            continue

        for next_dist, next_vertex in graph[vertex]:
            if mn_dist[next_vertex] > mn_dist[vertex] + next_dist:
                mn_dist[next_vertex] = mn_dist[vertex] + next_dist
                heapq.heappush(queue, (mn_dist[next_vertex], next_vertex))

    return mn_dist


T = int(input())
MAX = 1e9

for tc in range(1, T + 1):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B, D = map(int, input().split())

        graph[A].append((D, B))
        graph[B].append((D, A))

    from_S = bfs(S)
    from_G = bfs(G)
    from_H = bfs(H)

    answer = []

    for _ in range(T):
        X = int(input())

        if from_S[G] + from_G[H] + from_H[X] <= from_S[X]:
            answer.append(X)

        elif from_S[H] + from_H[G] + from_G[X] <= from_S[X]:
            answer.append(X)

    print(*sorted(answer))