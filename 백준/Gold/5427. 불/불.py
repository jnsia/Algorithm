def bfs(start):
    queue = deque(start)

    while queue:
        x, y, z = queue.popleft()

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < C and 0 <= ny < R:
                if z > -1 and maze[nx][ny] == '.' and maze[nx][ny] != '#':
                    maze[nx][ny] = '@'
                    queue.append([nx, ny, z + 1])

                if z == -1 and maze[nx][ny] != '*' and maze[nx][ny] != '#':
                    maze[nx][ny] = '*'
                    queue.append([nx, ny, z])
            else:
                if z > - 1:
                    print(z + 1)
                    return

    print('IMPOSSIBLE')


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for _ in range(T):
    R, C = map(int, input().split())

    maze = []
    start = []
    fire = []

    for r in range(C):
        line = list(input())

        for c in range(R):
            if line[c] == '@':
                start.append([r, c, 0])

            if line[c] == '*':
                fire.append([r, c, -1])

        maze.append(line)

    fire.extend(start)

    bfs(fire)