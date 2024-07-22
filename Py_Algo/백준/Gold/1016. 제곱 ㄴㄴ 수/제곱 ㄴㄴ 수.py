import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = int(M ** 0.5)

square = []

for i in range(2, L + 1):
    square.append(i ** 2)

dp = [1] * (M - N + 1)

for k in square:
    temp = ((N - 1) // k) + 1

    for j in range(temp * k, M + 1, k):
        dp[j - N] = 0

print(sum(dp))