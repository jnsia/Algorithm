def binary_search(low, high):
    result = -1

    while low <= high:
        mid = (low + high) // 2
        is_possible = bfs(mid)

        if is_possible:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def bfs(max_cost):
    min_cost = [MAX] * (N + 1)
    min_cost[A] = 0
    queue = [(0, A)]

    while queue:
        cost, vertex = heapq.heappop(queue)

        if cost > C:
            continue

        if cost > min_cost[vertex]:
            continue

        for next_cost, next_vertex in graph[vertex]:
            if next_cost > max_cost:
                continue

            if min_cost[next_vertex] > min_cost[vertex] + next_cost:
                min_cost[next_vertex] = min_cost[vertex] + next_cost
                heapq.heappush(queue, (min_cost[next_vertex], next_vertex))

    if min_cost[B] <= C:
        return True
    else:
        return False


import heapq

MAX = int(1e16)
N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, W = map(int, input().split())

    graph[S].append([W, E])
    graph[E].append([W, S])

answer = binary_search(0, int(1e9))
print(answer)
