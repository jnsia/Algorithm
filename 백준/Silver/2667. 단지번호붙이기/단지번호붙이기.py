def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
answer = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

answer.sort()

print(len(answer))
for i in answer:
    print(i)