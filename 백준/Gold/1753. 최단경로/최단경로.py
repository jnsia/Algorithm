import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
adj_arr = [[] for _ in range(V + 1)]

K = int(input())
max_num = 10 * 300000 * 20000
visited = [max_num for _ in range(V + 1)]
visited[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())

    adj_arr[u].append((w, v))

queue = []
heapq.heappush(queue, (0, K))

while queue:
    cost, node = heapq.heappop(queue)

    if cost > visited[node]:
        continue

    for next_cost, next_node in adj_arr[node]:
        if visited[next_node] > visited[node] + next_cost:
            visited[next_node] = visited[node] + next_cost
            heapq.heappush(queue, (visited[next_node], next_node))

for elem in range(1, V + 1):
    if visited[elem] == max_num:
        print('INF')
    else:
        print(visited[elem])