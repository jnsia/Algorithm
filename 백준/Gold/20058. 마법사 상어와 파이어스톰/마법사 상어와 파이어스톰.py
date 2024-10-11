import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    global result

    result += 1

    for d in range(4):
        nr = r + dx[d]
        nc = c + dy[d]

        if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N:
            if area[nr][nc] > 0:
                area[nr][nc] = 0
                dfs(nr, nc)


def melt():
    temp = [[area[i][j] for j in range(2 ** N)] for i in range(2 ** N)]

    for r in range(2 ** N):
        for c in range(2 ** N):
            ices = 0

            for d in range(4):
                nr = r + dx[d]
                nc = c + dy[d]

                if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N:
                    if area[nr][nc] > 0:
                        ices += 1

            if ices < 3:
                temp[r][c] = max(temp[r][c] - 1, 0)

    for r in range(2 ** N):
        for c in range(2 ** N):
            area[r][c] = temp[r][c]


def rotate(r, c, size):
    temp = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            temp[i][j] = area[(r + size - 1) - j][c + i]

    for i in range(size):
        for j in range(size):
            area[r + i][c + j] = temp[i][j]


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, Q = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

for q in range(Q):
    phase = L[q]
    size = 2 ** phase

    for r in range(0, 2 ** N, size):
        for c in range(0, 2 ** N, size):
            rotate(r, c, size)

    melt()

answer1 = 0
answer2 = 0

for r in range(2 ** N):
    for c in range(2 ** N):
        answer1 += area[r][c]

for r in range(2 ** N):
    for c in range(2 ** N):
        if area[r][c] > 0:
            result = 0
            area[r][c] = 0
            dfs(r, c)
            answer2 = max(answer2, result)

print(answer1, answer2, sep="\n")
