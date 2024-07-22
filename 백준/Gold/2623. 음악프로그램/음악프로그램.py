from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
preceding = [0] * (N + 1)

for _ in range(M):
    num, *singers = map(int, input().split())

    for idx in range(1, num):
        graph[singers[idx - 1]].append(singers[idx])
        preceding[singers[idx]] += 1

queue = deque()

for idx in range(1, N + 1):
    if preceding[idx] == 0:
        queue.append(idx)

cnt = 0
ans = []

while queue:
    vertex = queue.popleft()
    ans.append(vertex)
    cnt += 1

    for next_vertex in graph[vertex]:
        if preceding[next_vertex] == 1:
            queue.append(next_vertex)

        preceding[next_vertex] -= 1

if cnt == N:
    for i in ans:
        print(i)
else:
    print(0)