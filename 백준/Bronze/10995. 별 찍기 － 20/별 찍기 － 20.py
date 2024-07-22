N = int(input())

for i in range(1, N + 1):
    for j in range(1, N * 2 + 1):
        if (i + j) % 2:
            print(" ", end="")
        else:
            print('*', end="")
    print()