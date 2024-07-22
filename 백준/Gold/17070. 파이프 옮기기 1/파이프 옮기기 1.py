N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][0][0] = 1     # 가로
dp[0][1][0] = 1

for x in range(N):
    for y in range(1, N):
        if y + 1 < N and house[x][y + 1] == 0:
            dp[x][y + 1][0] = dp[x][y][0] + dp[x][y][2]

        if x + 1 < N and house[x + 1][y] == 0:
            dp[x + 1][y][1] = dp[x][y][1] + dp[x][y][2]

        if x + 1 < N and y + 1 < N and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
            dp[x + 1][y + 1][2] = dp[x][y][0] + dp[x][y][1] + dp[x][y][2]

print(sum(dp[N - 1][N - 1]))
