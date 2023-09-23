import heapq

MAX = 100000

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
min_cost = [MAX] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

queue = []

for start_cost, start_vertex in graph[1]:
    heapq.heappush(queue, (start_cost, start_vertex))

visited[1] =  1
max_cost = 0
answer = 0

for _ in range(N - 1):
    while queue:
        cost, vertex = heapq.heappop(queue)

        if visited[vertex]:
            continue

        for next_cost, next_vertex in graph[vertex]:
            heapq.heappush(queue, (next_cost, next_vertex))

        answer += cost
        visited[vertex] = 1

        if cost > max_cost:
            max_cost = cost

        break

print(answer - max_cost)