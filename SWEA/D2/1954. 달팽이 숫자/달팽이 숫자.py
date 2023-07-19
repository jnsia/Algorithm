T = int(input())

for t in range(1, T + 1):
    print(f'#{t}')
    N = int(input())

    numbers = [num for num in range(1, N * N + 1)]

    block = [-1 for i in range(N + 2)]
    block_map = [block[:] for j in range(N + 2)]

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            block_map[x][y] = 0

    a = 1
    b = 1

    while True:
        while block_map[a][b + 1] == 0:
            block_map[a][b] = numbers[0]
            b += 1
            del numbers[0]

        while block_map[a + 1][b] == 0:
            block_map[a][b] = numbers[0]
            a += 1
            del numbers[0]

        while block_map[a][b - 1] == 0:
            block_map[a][b] = numbers[0]
            b -= 1
            del numbers[0]
        
        while block_map[a - 1][b] == 0:
            block_map[a][b] = numbers[0]
            a -= 1
            del numbers[0]

        if len(numbers) == 1:
            block_map[a][b] = numbers[0]
            break

    for c in range(1, N + 1):
        for d in range(1, N + 1):
            print(block_map[c][d], end=' ')
        print()