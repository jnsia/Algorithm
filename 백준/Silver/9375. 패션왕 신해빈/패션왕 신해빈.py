import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    clothes = dict()

    for n in range(N):
        n, m = input().split()

        clothes.setdefault(m, [])
        clothes[m].append(n)

    com_sum = 1

    for value in clothes.values():
        com_sum = com_sum * (len(value) + 1)

    print(com_sum - 1)