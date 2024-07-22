def div(n, x, y):
    global cnt
    global r
    global c

    tmp = 2 ** (n - 1)

    if n == 1:
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                if i == r and j == c:
                    print(cnt)
                    exit()

                cnt += 1

    else:
        if x <= r < x + tmp and y <= c < y + tmp:
            div(n - 1, x, y)
        elif x <= r < x + tmp and y + tmp <= c < y + tmp * 2:
            cnt += tmp * tmp
            div(n - 1, x, y + tmp)
        elif x + tmp <= r < x + tmp * 2 and y <= c < y + tmp:
            cnt += tmp * tmp * 2
            div(n - 1, x + tmp, y)
        elif x + tmp <= r < x + tmp * 2 and y + tmp <= c < y + tmp * 2:
            cnt += tmp * tmp * 3
            div(n - 1, x + tmp, y + tmp)

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

cnt = 0

div(N, 0, 0)