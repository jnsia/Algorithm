def bfs(start):
    queue = deque(start)

    while queue:
        x, y, z = queue.popleft()

        if z > -1 and maze[x][y] != 'F' and (x in [0, R - 1] or y in [0, C - 1]):
            print(z + 1)
            return

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#':
                if z > -1 and maze[nx][ny] == '.':
                    maze[nx][ny] = ':'
                    queue.append([nx, ny, z + 1])

                if z == -1 and maze[nx][ny] != 'F':
                    maze[nx][ny] = 'F'
                    queue.append([nx, ny, z])

    print('IMPOSSIBLE')


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())

maze = []
start = []
fire = []

for r in range(R):
    line = list(input())

    for c in range(C):
        if line[c] == 'J':
            start.append([r, c, 0])

        if line[c] == 'F':
            fire.append([r, c, -1])

    maze.append(line)

start.extend(fire)

bfs(start)