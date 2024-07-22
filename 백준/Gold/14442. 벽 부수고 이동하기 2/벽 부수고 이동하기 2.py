def bfs():
    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
    visited[0][0][0] = 1
    queue = deque([[0, 0, 0]])

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            print(visited[z][x][y])
            return

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M:
                if plane[nx][ny] == 0 and visited[z][nx][ny] == 0:
                    queue.append([nx, ny, z])
                    visited[z][nx][ny] = visited[z][x][y] + 1

                if plane[nx][ny] == 1 and z < K and visited[z + 1][nx][ny] == 0:
                    queue.append([nx, ny, z + 1])
                    visited[z + 1][nx][ny] = visited[z][x][y] + 1

    print(-1)


import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().split())
plane = [list(map(int, list(input().rstrip()))) for _ in range(N)]
bfs()