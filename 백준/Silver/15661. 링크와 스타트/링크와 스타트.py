def stat(arr):
    stat_sum = 0

    for i in arr:
        for j in arr:
            if i != j:
                stat_sum += start_link[i][j]

    return stat_sum


def collect(idx):
    global min_diff
    
    if idx == N:
        start = []
        link = []

        for bit in range(N):
            if bits[bit]:
                start.append(bit)
            else:
                link.append(bit)

        if start and link:
            res = abs(stat(start) - stat(link))
            
            if min_diff > res:
                min_diff = res

        return

    bits[idx] = 1
    collect(idx + 1)

    bits[idx] = 0
    collect(idx + 1)


N = int(input())
start_link = [list(map(int, input().split())) for _ in range(N)]
bits = [0] * N
min_diff = 980309

collect(0)
print(min_diff)