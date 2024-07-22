import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 101

dp[1] = 1 # e
dp[2] = 1
dp[3] = 1 # e # d
dp[4] = 2 # e# a
dp[5] = 2 # b

for tc in range(1, T + 1):
    N = int(input())

    for i in range(6, 101):
        dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[N])