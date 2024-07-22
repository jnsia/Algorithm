T = int(input())

for t in range(1, T + 1):
    D, L, N = map(int, input().split())
    print(f'#{t}', end=" ")

    damage = 0

    for n in range(N):
        damage += D + (D * n * L // 100)

    print(damage)