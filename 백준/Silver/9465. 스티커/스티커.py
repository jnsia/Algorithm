T = int(input())

for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if N == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

        for idx in range(2, N):
            dp[0][idx] = sticker[0][idx] + max(dp[1][idx - 2], dp[1][idx - 1])
            dp[1][idx] = sticker[1][idx] + max(dp[0][idx - 2], dp[0][idx - 1])

        print(max(dp[0][N - 1], dp[1][N - 1]))