N = int(input())

for i in range(1, N * 2):
    for j in range(1, N + abs(N - i) + 1):
        if abs(i - N) < abs(j - N):
            print(" ", end="")
        else:
            print('*', end="")
    print()