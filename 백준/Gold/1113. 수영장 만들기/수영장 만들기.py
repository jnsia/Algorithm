from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
ground = [[0] * (M + 2) for _ in range(N + 2)]
max_ground = 0

for n in range(1, N + 1):
    line = list(map(int, input()))

    for m in range(1, M + 1):
        ground[n][m] = line[m - 1]
        max_ground = max(max_ground, line[m - 1])

answer = 0

for height in range(1, max_ground + 1):
    visited = [[False] * (M + 2) for _ in range(N + 2)]

    queue = deque()
    queue.append((height, 0, 0))

    while queue:
        h, x, y = queue.popleft()

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N + 2 and 0 <= ny < M + 2 and not visited[nx][ny]:
                visited[nx][ny] = True

                if ground[nx][ny] <= height:
                    queue.append((height, nx, ny))

    for i in range(N + 2):
        for j in range(M + 2):
            if not visited[i][j] and ground[i][j] <= height:
                answer += 1

print(answer)
