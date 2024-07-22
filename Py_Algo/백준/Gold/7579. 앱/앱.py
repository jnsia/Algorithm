N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

MAX = sum(cost)
dp = [[0] * MAX for _ in range(N + 1)]

for i in range(1, N + 1):
    m = memory[i - 1]
    c = cost[i - 1]

    for j in range(MAX):
        if j >= c:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + m)
        else:
            dp[i][j] = dp[i - 1][j]

answer = MAX

for idx in range(MAX):
    if dp[N][idx] >= M:
        answer = idx
        break

print(answer)
