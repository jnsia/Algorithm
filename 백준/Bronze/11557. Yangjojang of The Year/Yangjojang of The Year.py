T = int(input())

for _ in range(T):
    N = int(input())

    ms = ''
    ml = -1

    for _ in range(N):
        S, L = input().split()
        L = int(L)

        if L > ml:
            ms = S
            ml = L

    print(ms)