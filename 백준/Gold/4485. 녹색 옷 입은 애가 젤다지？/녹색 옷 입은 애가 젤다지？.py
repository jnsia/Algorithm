def bfs():
    cost_matrix = [[MAX] * N for _ in range(N)]
    cost_matrix[0][0] = cave[0][0]
    queue = [(0, 0, 0)]

    while queue:
        cost, x, y = heapq.heappop(queue)

        if cost > cost_matrix[x][y]:
            continue

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < N:
                if cost_matrix[nx][ny] > cost_matrix[x][y] + cave[nx][ny]:
                    cost_matrix[nx][ny] = cost_matrix[x][y] + cave[nx][ny]
                    heapq.heappush(queue, (cost_matrix[nx][ny], nx, ny))

    return cost_matrix[N - 1][N - 1]


import heapq

MAX = 125 * 125 * 9

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tc = 1

while True:
    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    result = bfs()
    print(f'Problem {tc}: {result}')
    tc += 1