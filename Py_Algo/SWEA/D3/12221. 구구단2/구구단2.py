T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{t}', end=" ")

    if N > 9 or M > 9:
        print(-1)
    else:
        print(N*M)


