def dfs(x, y, drc, res):
    global mx

    nx = x + dx[drc % 4]
    ny = y + dy[drc % 4]

    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
        if nx == i and ny == j:
            if len(res) > mx:
                # print(i, j, res)
                mx = len(res)
            return

        if cafe[nx][ny] in res:
            return

        visited[nx][ny] = True
        dfs(nx, ny, drc, res + [cafe[nx][ny]])

        if drc_visited[(drc + 1) % 4] == False:
            drc_visited[(drc + 1) % 4] = True
            dfs(nx, ny, drc + 1, res + [cafe[nx][ny]])
            drc_visited[(drc + 1) % 4] = False

        visited[nx][ny] = False
    else:
        return


dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    mx = -1

    for i in range(N):
        for j in range(N):
            drc_visited = [False] * 4
            for k in range(4):
                drc_visited[k] = True
                dfs(i, j, k, [cafe[i][j]])
                drc_visited[k] = False

    print(mx)