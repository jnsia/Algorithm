N = int(input())

dp = [0 for _ in range(10000)]
arr = [0 for _ in range(10000)]

for n in range(N):
    tmp = int(input())
    arr[n] = tmp


dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(dp[1], max(arr[0] + arr[2], arr[1] + arr[2]))

for i in range(3, N):
    dp[i] = max(dp[i - 1], max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]))

print(dp[N - 1])