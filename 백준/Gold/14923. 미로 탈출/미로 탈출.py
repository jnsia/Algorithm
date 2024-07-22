dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

maze = [[[0, 0] for _ in range(M)] for _ in range(N)]

for n in range(N):
    line = list(map(int, input().split()))
    for m in range(M):
        if line[m] == 1:
            maze[n][m][0] = -1
            maze[n][m][1] = -1

queue = [[Hx - 1, Hy - 1, 0]]
maze[Hx - 1][Hy - 1][0] = 1

while queue:
    x, y, cnt = queue.pop(0)

    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < N and 0 <= ny < M:
            if cnt == 0:
                if maze[nx][ny][0] == 0:
                    maze[nx][ny][0] = maze[x][y][0] + 1
                    queue.append([nx, ny, 0])

                if maze[nx][ny][0] == -1:
                    maze[nx][ny][1] = maze[x][y][0] + 1
                    queue.append([nx, ny, 1])
            elif cnt == 1:
                if maze[nx][ny][1] == 0:
                    maze[nx][ny][1] = maze[x][y][1] + 1
                    queue.append([nx, ny, 1])

print(min(maze[Ex - 1][Ey - 1]) - 1)
