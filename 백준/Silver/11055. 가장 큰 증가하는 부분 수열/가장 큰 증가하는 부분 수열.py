N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = arr[i]
    max_sum = 0

    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dp[j] > max_sum:
            max_sum = dp[j]

    dp[i] += max_sum

print(max(dp))