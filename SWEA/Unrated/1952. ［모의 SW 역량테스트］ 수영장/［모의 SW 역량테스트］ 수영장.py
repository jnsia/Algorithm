T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 12

    dp[0] = min(day * plan[0], month)
    dp[1] = min(dp[0] + day * plan[1], dp[0] + month)
    dp[2] = min(dp[1] + day * plan[2], dp[1] + month, three)

    for idx in range(3, 12):
        dp[idx] = min(dp[idx - 1] + day * plan[idx], dp[idx - 1] + month, dp[idx - 3] + three)

    print(min(dp[11], year))