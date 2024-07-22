T = int(input())

for tc in range(T):
    K = int(input())
    page = [0] + list(map(int, input().split()))
    prefix = [0] * (K + 1)

    for i in range(1, K + 1):
        prefix[i] = prefix[i - 1] + page[i]

    dp = [[0] * (K + 1) for _ in range(K + 1)]

    for i in range(2, K + 1):
        for j in range(1, K + 2 - i):
            min_value = float('inf')
            for k in range(i - 1):
                temp = dp[j][j + k] + dp[j + k + 1][j + i - 1]
                min_value = min(min_value, temp)
            dp[j][j + i - 1] = min_value + prefix[j + i - 1] - prefix[j - 1]

    print(dp[1][K])