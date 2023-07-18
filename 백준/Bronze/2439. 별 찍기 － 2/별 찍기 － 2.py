T = int(input())

for x in range(1, T + 1):
    for y in range(T):
        if x < T - y:
            print(' ', end="")
        else:
            print('*', end="")
    print()