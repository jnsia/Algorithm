def bfs(sx, sy):
    global mx_idx
    global mx_cnt

    queue = [[sx, sy]]
    cnt = 1

    while queue:
        x, y = queue.pop(0)

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < N and rooms[nx][ny] == rooms[x][y] + 1:
                queue.append([nx, ny])
                cnt += 1

    if mx_cnt < cnt:
        mx_cnt = cnt
        mx_idx = rooms[sx][sy]
        
    elif mx_cnt == cnt and mx_idx > rooms[sx][sy]:
        mx_idx = rooms[sx][sy]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    mx_idx = N * N + 1
    mx_cnt = 0

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(mx_idx, mx_cnt)