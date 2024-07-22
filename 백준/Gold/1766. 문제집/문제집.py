import heapq

N, M = map(int, input().split())
prev_cnt = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
hq = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    prev_cnt[B] += 1

for n in range(1, N + 1):
    if prev_cnt[n] == 0:
        heapq.heappush(hq, n)

while hq:
    vertex = heapq.heappop(hq)
    print(vertex, end=" ")

    for next_vertex in graph[vertex]:
        if prev_cnt[next_vertex] == 1:
            heapq.heappush(hq, next_vertex)

        prev_cnt[next_vertex] -= 1