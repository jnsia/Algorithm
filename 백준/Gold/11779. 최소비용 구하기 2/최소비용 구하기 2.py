import heapq

def bfs(start, end):
    visited = [100000001] * (N + 1)
    path = [[]] * (N + 1)
    visited[start] = 0
    path[start] = [start]
    queue = []
    heapq.heappush(queue, [start, 0])

    while queue:
        curr, curr_cost = heapq.heappop(queue)

        if visited[curr] < curr_cost:
            continue

        for dest, cost in route[curr]:
            if visited[dest] > visited[curr] + cost:
                visited[dest] = visited[curr] + cost
                path[dest] = path[curr] + [dest]
                heapq.heappush(queue, [dest, visited[curr] + cost])
        
    print(visited[end])
    print(len(path[end]))
    print(*path[end])


import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

route = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, K = map(int, input().split())
    route[A].append([B, K])

S, E = map(int, input().split())

bfs(S, E)