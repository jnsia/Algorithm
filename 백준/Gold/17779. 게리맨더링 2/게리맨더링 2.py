def init_area():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            test[r][c] = 0


def draw_five(x, y, d1, d2):
    for _ in range(d2):
        x = x + dr[0]
        y = y + dc[0]
        test[x][y] = 5

    for _ in range(d1):
        x = x + dr[1]
        y = y + dc[1]
        test[x][y] = 5

    for _ in range(d2):
        x = x + dr[2]
        y = y + dc[2]
        test[x][y] = 5

    for _ in range(d1):
        x = x + dr[3]
        y = y + dc[3]
        test[x][y] = 5

    for r in range(1, N + 1):
        flag = False
        temp = []

        for c in range(1, N + 1):
            if test[r][c] == 0 and flag:
                temp.append(c)
            elif test[r][c] == 5 and not flag:
                flag = True
            elif test[r][c] == 5 and flag:
                flag = False

        if not flag:
            for c in temp:
                test[r][c] = 5


def go(x, y, d1, d2):
    global answer

    init_area()
    draw_five(x, y, d1, d2)

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if test[r][c] == 5:
                continue

            if 1 <= r < x + d1 and 1 <= c <= y:
                test[r][c] = 1
            elif 1 <= r <= x+d2 and y < c <= N:
                test[r][c] = 2
            elif x+d1 <= r <= N and 1 <= c < y - d1 + d2:
                test[r][c] = 3
            elif x+d2 < r <= N and y - d1 + d2 <= c <= N:
                test[r][c] = 4

    count_list = [0, 0, 0, 0, 0]

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            count_list[test[r][c] - 1] += area[r - 1][c - 1]


    result = max(count_list) - min(count_list)
    answer = min(answer, result)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

N = int(input())
area = []
test = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# d1, d2 ≥ 1
# 1 ≤ x < x+d1+d2 ≤ N
# 1 ≤ y-d1 < y < y+d2 ≤ N

for _ in range(N):
    line = list(map(int, input().split()))
    area.append(line)

answer = 10000000

for r in range(1, N + 1):
    for c in range(1, N + 1):
        if r in (1, N) and c in (1, N):
            continue

        for d1 in range(1, N):
            for d2 in range(1, N):
                if r + d1 + d2 > N:
                    continue
                if c - d1 < 1 or c + d2 > N:
                    continue

                go(r, c, d1, d2)

print(answer)