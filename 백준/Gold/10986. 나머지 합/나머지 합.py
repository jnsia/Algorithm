N, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (N + 1)
mod_dp = [0] * M

for i in range(1, N + 1):
    dp[i] = (dp[i - 1] + arr[i - 1]) % M
    mod_dp[dp[i]] += 1

cnt = mod_dp[0]

for i in range(M):
    cnt += (mod_dp[i] * (mod_dp[i] - 1) // 2)

print(cnt)
