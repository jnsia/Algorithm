N, T = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(T + 1)]
tests = []

for _ in range(N):
    K, S = map(int, input().split())
    tests.append((K, S))

tests.sort(key=lambda x: x[0])

for j in range(1, T + 1):
    for i in range(1, N + 1):
        time, score = tests[i - 1]

        if j >= time:
            dp[j][i] = max(dp[j][i - 1], dp[j - time][i - 1] + score)
        else:
            dp[j][i] = dp[j][i - 1]

print(max(dp[T]))