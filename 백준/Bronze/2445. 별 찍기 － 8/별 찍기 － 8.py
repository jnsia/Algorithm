N = int(input())

for i in range(1, N * 2):
    for j in range(1, N * 4 + 1, 2):
        if abs(2 * N - j) <= 2 * abs(N - i):
            print(" ", end="")
        else:
            print('*', end="")
    print()