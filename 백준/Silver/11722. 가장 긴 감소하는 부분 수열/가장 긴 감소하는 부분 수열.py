N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    max_len = 0

    for j in range(i - 1, -1, -1):
        if arr[i] < arr[j] and dp[j] > max_len:
            max_len = dp[j]

    dp[i] = max_len + 1

print(max(dp))