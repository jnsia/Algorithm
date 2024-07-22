T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=" ")

    arr = []
    result = 'yes'
    rook = 0

    for x in range(8):
        li = list(input())
        arr.append(li)

        if li.count('O') > 1:
            result = 'no'

    for x in range(8):
        count = 0
        for y in range(8):
            if arr[y][x] == 'O':
                count += 1
                rook += 1
        if count > 1:
            result = 'no'

    if rook != 8:
        result = 'no'

    print(result)