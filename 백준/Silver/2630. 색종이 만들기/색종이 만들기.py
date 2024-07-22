def div(paper, num, x, y):
    global white
    global blue

    if num == 0:
        return 0

    tmp = num // 2

    w = 0
    b = 0

    for n in range(x, x + num):
        for m in range(y, y + num):
            if paper[n][m]:
                b += 1
            else:
                w += 1

    if w == num * num:
        white += 1
    elif b == num * num:
        blue += 1
    else:
        for i in range(x, x + num, tmp):
            for j in range(y, y + num, tmp):
                div(paper, tmp, i, j)

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

div(paper, N, 0, 0)
print(white, blue)