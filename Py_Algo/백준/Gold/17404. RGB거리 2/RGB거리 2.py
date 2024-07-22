N = int(input())
matrix = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

answer = int(1e9)

for color in range(3):
    dp = [[0, 0, 0] for _ in range(N + 1)]

    dp[1] = [int(1e9), int(1e9), int(1e9)]
    dp[1][color] = matrix[1][color]

    for idx in range(2, N + 1):
        dp[idx][0] = min(dp[idx - 1][1], dp[idx - 1][2]) + matrix[idx][0]
        dp[idx][1] = min(dp[idx - 1][0], dp[idx - 1][2]) + matrix[idx][1]
        dp[idx][2] = min(dp[idx - 1][0], dp[idx - 1][1]) + matrix[idx][2]

    dp[N][color] = int(1e9)
    answer = min(answer, min(dp[N]))

print(answer)