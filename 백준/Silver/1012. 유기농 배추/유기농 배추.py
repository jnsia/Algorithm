import sys
sys.setrecursionlimit(10**6)

default = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(a, b):
    for da, db in default:
        if 0 <= a + da < M and 0 <= b + db < N and dp[a+da][b+db] == 1:
            dp[a+da][b+db] = 0
            dfs(a+da, b+db)

import sys
input = sys.stdin.readline

T = int(input())


for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    dp = [[0 for _ in range(N)] for _ in range(M)]

    cnt = 0

    for k in range(K):
        x, y = map(int, input().split())

        dp[x][y] = 1

    for i in range(M):
        for j in range(N):
            if dp[i][j] == 1:
                cnt += 1
                dp[i][j] = 0
                dfs(i, j)
    print(cnt)