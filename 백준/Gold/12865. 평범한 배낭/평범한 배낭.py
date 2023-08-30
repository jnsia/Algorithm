N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
things = [[0, 0]]

for _ in range(N):
    weight, value = map(int, input().split())
    things.append([weight, value])

for x in range(1, N + 1):
    w, v = things[x]

    for y in range(1, K + 1):
        if y - w >= 0:
            dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - w] + v)
        else:
            dp[x][y] = dp[x - 1][y]

print(dp[N][K])