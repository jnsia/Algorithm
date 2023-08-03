T = 10

dy = [1, -1]

for tc in range(1, T + 1):
    tc_num = int(input())
    print(f'#{tc_num}', end=" ")

    ladder = []

    x = 99
    y = 0

    for _ in range(100):
        temp_list = list(map(int, input().split()))
        ladder.append(temp_list)

        if 2 in temp_list:
            y = temp_list.index(2)

    while x > 0:
        ly = y - 1
        ry = y + 1

        if 0 <= ly < 100 and ladder[x][ly] == 1:
            ladder[x][y] = 0
            y -= 1
        elif 0 <= ry < 100 and ladder[x][ry] == 1:
            ladder[x][y] = 0
            y += 1
        elif ladder[x - 1][y] == 1:
            x -= 1

    print(y)
