import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

W, H = map(int, input().split())

board = []

sx, sy = -1, -1
ex, ey = -1, -1

for h in range(H):
    row = input()

    for w in range(W):
        if row[w] == 'C':
            if sx == sy == -1:
                sx, sy = h, w
            else:
                ex, ey = h, w

    board.append(row)

queue = []

visited = [[[10001] * 4 for _ in range(W)] for _ in range(H)]

for d in range(4):
    visited[sx][sy][d] = 0
    heapq.heappush(queue, (0, d, sx, sy))

while queue:
    m, d, x, y = heapq.heappop(queue)

    for i in range(-1, 2):
        nm = m + abs(i)
        nd = (d + i + 4) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
            if visited[nx][ny][nd] > nm:
                visited[nx][ny][nd] = nm
                queue.append((nm, nd, nx, ny))

print(min(visited[ex][ey]))