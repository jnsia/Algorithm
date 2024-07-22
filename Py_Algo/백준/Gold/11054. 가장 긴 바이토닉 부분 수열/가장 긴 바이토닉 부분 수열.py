N = int(input())
arr = list(map(int, input().split()))

dp = [[1, 1] for _ in range(N)]

for i in range(1, N):
    max_num = 0

    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dp[j][0] > max_num:
            max_num = dp[j][0]

    dp[i][0] = max_num + 1

for i in range(N - 1, -1, -1):
    max_num = 0

    for k in range(i, N):
        if arr[i] > arr[k] and dp[k][1] > max_num:
            max_num = dp[k][1]

    dp[i][1] = max_num + 1

ans = 0

for len in dp:
    res = sum(len) - 1

    if res > ans:
        ans = res

print(ans)