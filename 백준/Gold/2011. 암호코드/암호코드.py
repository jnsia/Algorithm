encode = list(map(int, input()))
N = len(encode)

dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 1

if not encode[0]:
    print(0)
else:
    for idx in range(1, N):
        if encode[idx]:
            dp[idx + 1] += dp[idx]

        tmp = encode[idx - 1] * 10 + encode[idx]

        if 10 <= tmp <= 26:
            dp[idx + 1] += dp[idx - 1]

        dp[idx + 1] %= 1000000

    print(dp[N])
