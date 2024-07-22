def star(x, y, n):
    if n == 3:
        stars[x][y] = '*'
        stars[x + 1][y - 1] = '*'
        stars[x + 1][y + 1] = '*'
        for z in range(-2, 3):
            stars[x + 2][y + z] = '*'
    else:
        star(x, y, n // 2)
        star(x + n // 2, y - n // 2, n // 2)
        star(x + n // 2, y + n // 2, n // 2)


N = int(input())
stars = [[' '] * (N * 2) for _ in range(N)]

star(0, N - 1, N)

for line in stars:
    print(*line, end="", sep="")
    print()
