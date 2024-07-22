import sys
input = sys.stdin.readline

T = int(input())

default_dict = {0: [1, 0], 1: [0, 1]}

for i in range(2, 41):
    default_dict[i] = [
        default_dict[i - 2][0] + default_dict[i - 1][0],
        default_dict[i - 2][1] + default_dict[i - 1][1],
    ]

for t in range(T):
    N = int(input())

    print(*default_dict[N])