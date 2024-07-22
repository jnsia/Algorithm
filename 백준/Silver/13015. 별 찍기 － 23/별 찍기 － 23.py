N = int(input())

for i in range(1, N * 2):
    print(' ' * (N - abs(N - i) - 1), end="")

    if i == 1 or i == N * 2 - 1:
        print('*' * N, end="")
        print(' ' * (abs(N - i) * 2 - 1), end="")
        print('*' * N, end="")
    elif i == N:
        print('*' + ' ' * (N - 2) + '*' + ' ' * (N - 2) + '*', end="")
    else:
        print('*' + ' ' * (N - 2) + '*', end="")
        print(' ' * (abs(N - i) * 2 - 1), end="")
        print('*' + ' ' * (N - 2) + '*', end="")

    print()