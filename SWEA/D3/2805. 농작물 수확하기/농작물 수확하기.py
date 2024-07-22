T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    harvest_sum = 0

    for i in range(N):
        for j in range(N):
            if abs(N // 2 - j) + abs(N // 2 - i) <= N // 2:
                harvest_sum += farm[i][j]

    print(harvest_sum)