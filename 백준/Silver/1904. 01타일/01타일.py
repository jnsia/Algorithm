import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1000001
dp[1] = 1 # 1C1
dp[2] = 2 # 2C0 + 1C1

for i in range(3, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N] % 15746)