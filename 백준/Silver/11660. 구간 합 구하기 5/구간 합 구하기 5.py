import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    lst = list(map(int, input().split()))

    for j in range(1, N + 1):
        dp[i][j] = lst[j - 1]

for x in range(1, N + 1):
    for y in range(1, N):
        dp[x][y + 1] += dp[x][y]
    
for w in range(1, N):
    for v in range(1, N + 1):
        dp[w + 1][v] += dp[w][v]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    res = dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1]) + dp[x1 - 1][y1 - 1]
    print(res)