def dfs(idx, res, cnt):
    global ans

    if idx == N:
        if res == M and cnt > 0:
            ans += 1
        return

    dfs(idx + 1, res + arr[idx], cnt + 1)
    dfs(idx + 1, res, cnt)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)

print(ans)
