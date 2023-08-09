def bfs(start):
    global arr
    queue = [start]
    dp = [[18*N for _ in range(N)] for _ in range(N)]
    dp[0][0] = 0

    while queue:
        tmp_coord = queue.pop(0)
        x = tmp_coord[0]
        y = tmp_coord[1]

        if arr[x][y] > 18 * N:
            continue

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0:
                    continue
                elif dp[nx][ny] == -1:
                    dp[nx][ny] = arr[nx][ny] + dp[x][y]
                    queue.append((nx, ny))
                else:
                    if dp[nx][ny] > arr[nx][ny] + dp[x][y]:
                        dp[nx][ny] = arr[nx][ny] + dp[x][y]
                        queue.append((nx, ny))

    return dp[N-1][N-1]

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    arr = []

    for _ in range(N):
        tmp_arr = list(map(int, list(input())))
        arr.append(tmp_arr)

    print(bfs((0, 0)))
