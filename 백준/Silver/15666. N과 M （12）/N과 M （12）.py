def subset(res, depth):
    if depth == N or len(res) == M:
        print(*res)
        return

    collected = set()

    for idx in range(N):
        if arr[idx] not in collected:
            if not res or res[-1] <= arr[idx]:
                collected.add(arr[idx])
                subset(res + [arr[idx]], depth + 1)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

subset([], 0)