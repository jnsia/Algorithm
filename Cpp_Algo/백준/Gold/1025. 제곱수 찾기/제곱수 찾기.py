import math

N, M = map(int, input().split())
board = [input() for _ in range(N)]

res = -1

for i in range(N):
    for j in range(M):
        for a in range(-N, N):
            for b in range(-M, M):
                if a == 0 and b == 0:
                    continue

                num = ''
                x, y = i, j

                while 0 <= x < N and 0 <= y < M:
                    num += board[x][y]
                    temp = math.sqrt(int(num))

                    if temp == int(temp):
                        res = max(int(num), res)

                    x += a
                    y += b

print(res)
