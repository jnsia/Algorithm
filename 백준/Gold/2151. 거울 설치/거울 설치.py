from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

MAX = 10001

N = int(input())
board = [input() for _ in range(N)]
visited = [[[MAX] * 4 for _ in range(N)] for _ in range(N)]

sx, sy = -1, -1
ex, ey = -1, -1

for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            if sx == sy == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

queue = deque()

for sz in range(4):
    queue.append((sx, sy, sz, 0))
    visited[sx][sy][sz] = 0

while queue:
    x, y, z, c = queue.popleft()

    nx = x + dx[z]
    ny = y + dy[z]

    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != '*':
        if board[nx][ny] == '!':
            if visited[nx][ny][(z + 3) % 4] >= c + 1:
                queue.append((nx, ny, (z + 3) % 4, c + 1))
                visited[nx][ny][(z + 3) % 4] = c + 1

            if visited[nx][ny][(z + 1) % 4] >= c + 1:
                queue.append((nx, ny, (z + 1) % 4, c + 1))
                visited[nx][ny][(z + 1) % 4] = c + 1

        if visited[nx][ny][z] >= c:
            queue.appendleft((nx, ny, z, c))
            visited[nx][ny][z] = c

print(min(visited[ex][ey]))