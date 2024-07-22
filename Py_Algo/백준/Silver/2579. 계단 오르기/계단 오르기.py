N = int(input())
stare = []
dp = [0] * N

for n in range(N):
    tmp = int(input())
    stare.append(tmp)

if N == 1:
    print(stare[0])
elif N == 2:
    print(max(stare[0] + stare[1], stare[1]))
else:
    dp[0] = stare[0]
    dp[1] = max(stare[0] + stare[1], stare[1])
    dp[2] = max(stare[0] + stare[2], stare[1] + stare[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stare[i], dp[i - 3] + stare[i - 1] + stare[i])

    print(dp[N - 1])