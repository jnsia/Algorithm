import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [10000001] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for j in range(i, N + 1):
        dp[j] = min(dp[j], dp[j - i] + P[i])

print(dp[N])