def dfs(x, y):
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


import sys
sys.setrecursionlimit(100001)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(101):
    visited = [[False] * N for _ in range(N)]

    result = 0

    for j in range(N):
        for k in range(N):
            if board[j][k] <= i:
                visited[j][k] = True

    for j in range(N):
        for k in range(N):
            if not visited[j][k]:
                visited[j][k] = True
                dfs(j, k)
                result += 1

    answer = max(answer, result)

print(answer)
