def calc(nx, ny, q, percent):
    temp = int(q * percent)
    landing(nx, ny, temp)
    return temp


def landing(nx, ny, q):
    global answer

    if 0 <= nx < N and 0 <= ny < N:
        grid[nx][ny] += q


def spread(r, c, q, d):
    grid[r][c] -= q
    total = q

    nr = r + dx[d] * 2
    nc = c + dy[d] * 2

    total -= calc(nr, nc, q, 0.05)

    for w in [-1, 1]:
        nr = r + dx[d] + dx[(d + w) % 4]
        nc = c + dy[d] + dy[(d + w) % 4]

        total -= calc(nr, nc, q, 0.1)

    for w in [-1, 1]:
        nr = r + dx[(d + w) % 4]
        nc = c + dy[(d + w) % 4]

        total -= calc(nr, nc, q, 0.07)

    for w in [-1, 1]:
        nr = r + dx[(d + w) % 4] * 2
        nc = c + dy[(d + w) % 4] * 2

        total -= calc(nr, nc, q, 0.02)

    for w in [-1, 1]:
        nr = r + dx[(d + 2) % 4] + dx[(d + w) % 4]
        nc = c + dy[(d + 2) % 4] + dy[(d + w) % 4]

        total -= calc(nr, nc, q, 0.01)

    # 남은 모래는 다음 칸으로 이동
    nr = r + dx[d]
    nc = c + dy[d]

    landing(nr, nc, total)


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N = int(input())

directions = [[0 for _ in range(N)] for _ in range(N)]
grid = [list(map(int, input().split())) for _ in range(N)]

count = 0
horizontal = 1
vertical = 1

x = N // 2
y = N // 2

answer = 0

for line in grid:
    answer += sum(line)

while True:
    if horizontal == vertical:
        # move to horizontal
        if y >= N // 2:
            # move to left
            for _ in range(min(horizontal, N - 1)):
                y -= 1
                directions[x][y] = 0
                spread(x, y, grid[x][y], 0)
        else:
            # move to right
            for _ in range(min(horizontal, N - 1)):
                y += 1
                directions[x][y] = 2
                spread(x, y, grid[x][y], 2)

        horizontal += 1
    else:
        # move to vertical
        if x > N // 2:
            # move to up
            for _ in range(min(vertical, N - 1)):
                x -= 1
                directions[x][y] = 3
                spread(x, y, grid[x][y], 3)
        else:
            # move to down
            for _ in range(min(vertical, N - 1)):
                x += 1
                directions[x][y] = 1
                spread(x, y, grid[x][y], 1)

        vertical += 1

    if x == 0 and y == 0:
        break

for line in grid:
    answer -= sum(line)

print(answer)