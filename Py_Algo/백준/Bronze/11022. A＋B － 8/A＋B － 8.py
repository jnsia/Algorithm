T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())

    print(f'Case #{t}: {n} + {m} = {n + m}')
    