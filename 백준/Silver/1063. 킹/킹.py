dirt = { "R": 0, "L": 1, "B": 2, "T": 3, "RT": 4, "LT": 5, "RB": 6, "LB": 7 }
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
map = [[0] * 8 for _ in range(8)]

king, rock, N = input().split()

king = [8 - int(king[1]), ord(king[0]) - ord('A')]
rock = [8 - int(rock[1]), ord(rock[0]) - ord('A')]
N = int(N)

map[king[0]][king[1]] = 1
map[rock[0]][rock[1]] = -1

for _ in range(N):
    cmd = input()

    kx, ky = king
    rx, ry = rock

    nkx = kx + dx[dirt[cmd]]
    nky = ky + dy[dirt[cmd]]

    if nkx > 7 or nkx < 0 or nky > 7 or nky < 0:
        continue

    if map[nkx][nky] == -1:
        nrx = rx + dx[dirt[cmd]]
        nry = ry + dy[dirt[cmd]]

        if nrx > 7 or nrx < 0 or nry > 7 or nry < 0:
            continue

        map[rx][ry] = 0
        rock = [nrx, nry]
        map[nrx][nry] = -1

    map[kx][ky] = 0
    king = [nkx, nky]
    map[nkx][nky] = 1

print(chr(king[1] + ord('A')), 8 - king[0], sep="")
print(chr(rock[1] + ord('A')), 8 - rock[0], sep="")
