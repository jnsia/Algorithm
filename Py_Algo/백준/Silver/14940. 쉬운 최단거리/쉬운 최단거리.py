def bfs(start):
    global total_map
    queue = [start]
    num = 0
    dp = [[-1 for _ in range(M)] for _ in range(N)]

    while queue:
        num += 1
        for _ in range(len(queue)):
            tmp_coord = queue.pop(0)

            for z in range(4):
                nx = tmp_coord[0] + dx[z]
                ny = tmp_coord[1] + dy[z]

                if 0 <= nx < N and 0 <= ny < M:
                    if nx == start[0] and ny == start[1]:
                        dp[nx][ny] = 0
                    elif total_map[nx][ny] == 0:
                        dp[nx][ny] = 0
                    elif dp[nx][ny] == -1:
                        dp[nx][ny] = num
                        queue.append((nx, ny))

    return dp

N, M = map(int, input().split())

target = ()
total_map =[]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tmp_idx in range(N):
    tmp_arr = list(map(int, input().split()))

    if 2 in tmp_arr:
        target = (tmp_idx, tmp_arr.index(2))

    total_map.append(tmp_arr)

res_map = bfs(target)

for x in range(N):
    for y in range(M):
        if total_map[x][y] == 0:
            res_map[x][y] = 0

for res in res_map:
    print(*res)