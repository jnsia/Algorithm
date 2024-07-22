def stat(arr):
    stat_sum = 0

    for i in arr:
        for j in arr:
            if i != j:
                stat_sum += start_link[i - 1][j - 1]

    return stat_sum


def collect(depth, start, collected):
    global min_diff
    tmp_collected = collected[:]
    
    if depth == N // 2:
        link = []

        for player2 in range(1, N + 1):
            if player2 not in start:
                link.append(player2)

        res = abs(stat(start) - stat(link))
        
        if min_diff > res:
            min_diff = res

        return

    for player in range(1, N + 1):
        if collected[player] == False:
            tmp_collected[player] = True
            collect(depth + 1, start + [player], tmp_collected)


N = int(input())
start_link = [list(map(int, input().split())) for _ in range(N)]
collected = [False] * (N + 1)
min_diff = 980309

collect(0, [], collected)
print(min_diff)