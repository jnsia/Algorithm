N, M, K = map(int, input().split())
chess = [[0] * M for _ in range(N)]
prefix = [[0] * (M + 1) for _ in range(N + 1)]

ref = ['W', 'B']

for n in range(N):
    line = list(input())

    for m in range(M):
        if line[m] == ref[(n + m) % 2]:
            chess[n][m] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] + chess[i - 1][j - 1] - prefix[i - 1][j - 1]

mn_ans = K * K

for i in range(K, N + 1):
    for j in range(K, M + 1):
        ans = prefix[i][j] - prefix[i][j - K] - prefix[i - K][j] + prefix[i - K][j - K]

        mn_ans = min(mn_ans, ans, K * K - ans)

print(mn_ans)