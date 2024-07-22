def dfs(idx, res):
    global ans

    if ans:
        return

    for i in range(1, idx // 2 + 1):
        if res[idx - i * 2: idx - i] == res[idx - i:]:
            return

    if idx == N:
        ans = res
        return

    for i in range(1, 4):
        dfs(idx + 1, res + str(i))


N = int(input())

ans = ''
dfs(0, '')
print(ans)