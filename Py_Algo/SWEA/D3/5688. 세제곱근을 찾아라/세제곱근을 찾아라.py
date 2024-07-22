T = int(input())

dp = [0] * 10000001

for i in range(1, 1000001):
    dp[i] = i ** 3

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}', end=" ")

    if N not in dp:
        print(-1)
    else:
        print(dp.index(N))