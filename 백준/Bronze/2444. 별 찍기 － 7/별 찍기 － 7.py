N = int(input())

for i in range(1, 2 * N):
    if i > N:
        for j in range(1, N * 3 - i):
            if i - j < N:
                print('*', end="")
            else:
                print(' ', end="")
    else:
        for j in range(1, N + i):
            if i + j > N:
                print('*', end="")
            else:
                print(' ', end="")
    print()