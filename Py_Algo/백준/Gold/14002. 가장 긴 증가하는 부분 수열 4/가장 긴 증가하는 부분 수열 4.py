N = int(input())
arr = list(map(int, input().split()))

dp = [[1, [arr[idx]]] for idx in range(N)]

for i in range(1, N):
    max_len = 0
    route = []

    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dp[j][0] > max_len:
            max_len = dp[j][0]
            route = dp[j][1]

    dp[i][0] = max_len + 1
    dp[i][1] = route + dp[i][1]

ans = max(dp)

print(ans[0])
print(*ans[1])