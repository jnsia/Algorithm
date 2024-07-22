def dfs(i, j):
    global res

    if j == 6:
        i = i + 1
        j = i + 1

    if i == 5:
        res = 1

        for k in group:
            if k != 0:
                res = 0

        return

    # i 승
    if group[i * 3] > 0 and group[j * 3 + 2] > 0:
        group[i * 3] -= 1
        group[j * 3 + 2] -= 1
        dfs(i, j + 1)
        group[i * 3] += 1
        group[j * 3 + 2] += 1

    # i 무승부
    if group[i * 3 + 1] > 0 and group[j * 3 + 1] > 0:
        group[i * 3 + 1] -= 1
        group[j * 3 + 1] -= 1
        dfs(i, j + 1)
        group[i * 3 + 1] += 1
        group[j * 3 + 1] += 1

    # i 패
    if group[i * 3 + 2] > 0 and group[j * 3] > 0:
        group[i * 3 + 2] -= 1
        group[j * 3] -= 1
        dfs(i, j + 1)
        group[i * 3 + 2] += 1
        group[j * 3] += 1


for game in range(4):
    group = list(map(int, input().split()))
    res = 0

    dfs(0, 1)

    print(res, end=" ")
