N = int(input())

for i in range(N):
    for j in range(N):
        if N - j > i:
            print('*', end="")
    print()