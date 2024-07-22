N = int(input())

for i in range(1, N + 1):
    for j in range(1, i + N):
        if N - i >= j:
            print(" ", end="")
        else:
            print('*', end="")
    print()