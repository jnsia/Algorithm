N = int(input())

for i in range(1, N * 2):
    for j in range(1, N + 1):
        if abs(i - N) >= j:
            print(" ", end="")
        else:
            print('*', end="")
    print()

    