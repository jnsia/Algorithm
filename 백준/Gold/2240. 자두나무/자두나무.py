T, W = map(int, input().split())
dp = [[0] * (W + 2) for _ in range(T + 1)]

for idx in range(T):
    location = int(input())

    for move in range(1, W + 2):
        if move % 2 == location % 2:
            dp[idx + 1][move] = max(dp[idx][move - 1], dp[idx][move]) + 1
        else:
            dp[idx + 1][move] = dp[idx][move]
            
print(max(dp[T]))