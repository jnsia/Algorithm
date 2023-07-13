T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    result = []

    for i in range(N):
        li = list(map(int, input().split()))
        arr.append(li)

    for x in range(N):
        count = 0
        for y in range(N):
            if arr[x][y] == 1:
                count += 1
            elif arr[x][y] == 0:
                result.append(count)
                count = 0
        result.append(count)

    for x in range(N):
        count = 0
        for y in range(N):
            if arr[y][x] == 1:
                count += 1
            elif arr[y][x] == 0:
                result.append(count)
                count = 0
        result.append(count)
    print(f'#{t}', result.count(M))
