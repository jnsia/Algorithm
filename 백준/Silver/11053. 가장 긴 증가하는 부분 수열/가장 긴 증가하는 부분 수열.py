N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
    max_num = 0

    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dp[j] > max_num:
            max_num = dp[j]

    dp[i] = max_num + 1

# print(dp)
print(max(dp))