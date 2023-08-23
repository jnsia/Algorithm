def left_count(matrix):
    cnt = 0

    for x in range(W):
        for y in range(H):
            if matrix[x][y]:
                cnt += 1

    return cnt


def detect_target(depth, templete):
    global mn

    if left_count(templete) == 0:
        mn = 0
        return

    if depth == N:
        res = left_count(templete)

        if mn > res:
            mn = res

        return

    for x in range(W):
        new_blocks = [line[:] for line in templete]
        for y in range(H):
            if new_blocks[x][0] == 0:
                break

            elif y == H - 1 or new_blocks[x][y + 1] == 0:
                break_block(x, y, new_blocks)
                new_blocks = gravity(new_blocks)
                detect_target(depth + 1, new_blocks)
                break




def gravity(map):
    for line in map:
        if 0 in line:
            for _ in range(H):
                line.remove(0)
                line.append(0)

    return map


def break_block(x, y, matrix):
    target = matrix[x][y]
    matrix[x][y] = 0

    for move in range(4):
        for boom in range(1, target):
            nx = x + dx[move] * boom
            ny = y + dy[move] * boom

            if 0 <= nx < W and 0 <= ny < H and matrix[nx][ny]:
                break_block(nx, ny, matrix)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, W, H = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(H)]
    blocks = list(map(list, zip(*tmp[::-1])))

    mn = 19980309
    detect_target(0, blocks)
    print(mn)