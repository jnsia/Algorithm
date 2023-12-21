def dfs(idx):
    global answer

    if idx == 8:

        for i in range(8):
            curr = arr[i]
            prev = arr[(i + 7) % 8]
            next_stat = arr[(i + 9) % 8]

            if (prev * next_stat) / (prev + next_stat) > curr / (2 ** 0.5):
                return

        answer += 1
        return

    for jdx in range(8):
        if not collected[jdx]:
            collected[jdx] = True
            arr[idx] = stats[jdx]
            dfs(idx + 1)
            collected[jdx] = False


stats = list(map(int, input().split()))
arr = [0] * 8
collected = [False] * 8
answer = 0
dfs(0)
print(answer)
