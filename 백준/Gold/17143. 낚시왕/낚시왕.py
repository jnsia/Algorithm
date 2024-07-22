def move_shark(x, y, direction, speed):

    if direction > 1:
        speed = speed % (2 * (C - 1))
        move = dy[direction]

        for _ in range(speed):
            y += move

            if y == -1:
                y = 1
                move = -move
            elif y == C:
                y = C - 2
                move = -move

        if move == -1:
            return x, y, 3
        else:
            return x, y, 2
    else:
        speed = speed % (2 * (R - 1))
        move = dx[direction]

        for _ in range(speed):
            x += move

            if x == -1:
                x = 1
                move = -move
            elif x == R:
                x = R - 2
                move = -move

        if move == -1:
            return x, y, 0
        else:
            return x, y, 1


def catch(location):
    global answer

    key = 0
    catch_shark = 0

    while key < R and not catch_shark:
        catch_shark = ocean[key][location][0]
        key += 1

    if catch_shark:
        ocean[key - 1][location] = [0, 0, 0]
        answer += catch_shark


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C, M = map(int, input().split())

# 크기, 이동 방향, 속력
ocean = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
queue = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())

    ocean[r - 1][c - 1][0] = z
    ocean[r - 1][c - 1][1] = d - 1
    ocean[r - 1][c - 1][2] = s


answer = 0

for idx in range(C):
    catch(idx)
    # print(ocean)

    new_ocean = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if ocean[r][c][0]:
                nr, nc, nd = move_shark(r, c, ocean[r][c][1], ocean[r][c][2])

                if new_ocean[nr][nc][0] < ocean[r][c][0]:
                    new_ocean[nr][nc][0] = ocean[r][c][0]
                    new_ocean[nr][nc][1] = nd
                    new_ocean[nr][nc][2] = ocean[r][c][2]

    ocean = new_ocean

# print(ocean)
print(answer)
