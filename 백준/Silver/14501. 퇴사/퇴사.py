N = int(input())
dp = [0 for _ in range(N + 1)]
mx_val = 0

for idx in range(N):
    period, profit = map(int, input().split())

    for jdx in range(idx + period, N + 1):
        if dp[jdx] < dp[idx] + profit:
            dp[jdx] = dp[idx] + profit

print(max(dp))