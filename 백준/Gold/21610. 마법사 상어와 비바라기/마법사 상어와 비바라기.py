import sys
input = sys.stdin.readline
from collections import deque

dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])
visited = [[False] * N for _ in range(N)]

for _ in range(M):
    D, S = map(int, input().split())

    for _ in range(len(queue)):
        x, y = queue.popleft()

        nx = (x + dx[D - 1] * S + N) % N
        ny = (y + dy[D - 1] * S + N) % N

        visited[nx][ny] = True

        matrix[nx][ny] += 1


    for r in range(N):
        for c in range(N):
            if visited[r][c] == True:
                for dr, dc in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc]:
                        matrix[r][c] += 1

    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and visited[i][j] == False:
                queue.append((i, j))
                matrix[i][j] -= 2

            if visited[i][j]:
                visited[i][j] = False

total_water = 0

for i in range(N):
    for j in range(N):
        total_water += matrix[i][j]

print(total_water)