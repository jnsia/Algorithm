def dfs(x, y):
    global temp

    temp += 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < M and 0 <= ny < N and not paper[nx][ny]:
            paper[nx][ny] = 1
            dfs(nx, ny)


from sys import *
setrecursionlimit(10**5)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N, K = map(int, input().split())

paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for i in range(y1, y2):
            paper[i][j] = 1

answer = 0
result = []
temp = 0

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            temp = 0
            answer += 1
            paper[i][j] = 1
            dfs(i, j)
            result.append(temp)

print(answer)
print(*sorted(result))