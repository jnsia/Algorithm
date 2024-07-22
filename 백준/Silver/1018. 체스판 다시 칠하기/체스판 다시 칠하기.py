def black_white(map):
    x_prev = ''
    y_prev = ''

    count = 0

    if map[0][0] == 'W':
        map[0][0] = 'B'
        count += 1

    for x in range(8):
        if x_prev == map[x][0]:
            if map[x][0] == 'B':
                map[x][0] = 'W'
                count += 1
            elif map[x][0] == 'W':
                map[x][0] = 'B'
                count += 1

        y_prev = map[x][0]

        for y in range(1, 8):
            if map[x][y] == y_prev:
                if map[x][y] == 'B':
                    map[x][y] = 'W'
                    count += 1
                elif map[x][y] == 'W':
                    map[x][y] = 'B'
                    count += 1
            
            y_prev = map[x][y]

        x_prev = map[x][0]

    return count

def white_black(map):
    x_prev = ''
    y_prev = ''

    count = 0

    if map[0][0] == 'B':
        map[0][0] = 'W'
        count += 1

    for x in range(8):
        if x_prev == map[x][0]:
            if map[x][0] == 'B':
                map[x][0] = 'W'
                count += 1
            elif map[x][0] == 'W':
                map[x][0] = 'B'
                count += 1

        y_prev = map[x][0]

        for y in range(1, 8):
            if map[x][y] == y_prev:
                if map[x][y] == 'B':
                    map[x][y] = 'W'
                    count += 1
                elif map[x][y] == 'W':
                    map[x][y] = 'B'
                    count += 1
            
            y_prev = map[x][y]

        x_prev = map[x][0]

    return count

n, m = map(int, input().split())
total_map = [list(input()) for _ in range(n)]
BW_map = [[0 for _ in range(8)] for _ in range(8)]
WB_map = [[0 for _ in range(8)] for _ in range(8)]

arr = []

for i in range(n - 7):
    for j in range(m - 7):
        for k in range(8):
            for l in range(8):
                BW_map[k][l] = total_map[k + i][l + j]
                WB_map[k][l] = total_map[k + i][l + j]
        arr.append(black_white(BW_map))
        arr.append(white_black(WB_map))

print(min(arr))