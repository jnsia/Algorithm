def up():
    global x
    global z

    z = '^'
    plane[x][y] = z

    if x - 1 >= 0 and plane[x - 1][y] == '.':
        plane[x][y], plane[x - 1][y] = plane[x - 1][y], plane[x][y]
        x -= 1


def down():
    global x
    global z

    z = 'v'
    plane[x][y] = z

    if x + 1 < H and plane[x + 1][y] == '.':
        plane[x][y], plane[x + 1][y] = plane[x + 1][y], plane[x][y]
        x += 1


def left():
    global y
    global z

    z = '<'
    plane[x][y] = z

    if y - 1 >= 0 and plane[x][y - 1] == '.':
        plane[x][y], plane[x][y - 1] = plane[x][y - 1], plane[x][y]
        y -= 1


def right():
    global y
    global z

    z = '>'
    plane[x][y] = z

    if y + 1 < W and plane[x][y + 1] == '.':
        plane[x][y], plane[x][y + 1] = plane[x][y + 1], plane[x][y]
        y += 1


def shoot():
    global z

    num = 1

    while True:
        nx = x + direction[z][0] * num
        ny = y + direction[z][1] * num

        if 0 <= nx < H and 0 <= ny < W:
            if plane[nx][ny] == '*':
                plane[nx][ny] = '.'
                return

            if plane[nx][ny] == '#':
                return

            num += 1
        else:
            return


direction = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    H, W = map(int, input().split())
    plane = []

    x = 0
    y = 0
    z = ''

    for h in range(H):
        line = list(input())
        for w in range(W):
            if line[w] in ['^', 'v', '<', '>']:
                x, y, z = h, w, line[w]
        plane.append(line)

    N = int(input())
    cmd_list = input()

    for idx in range(N):
        if cmd_list[idx] == 'U':
            up()

        if cmd_list[idx] == 'D':
            down()

        if cmd_list[idx] == 'L':
            left()

        if cmd_list[idx] == 'R':
            right()

        if cmd_list[idx] == 'S':
            shoot()

    for line in plane:
        print(*line, sep="")