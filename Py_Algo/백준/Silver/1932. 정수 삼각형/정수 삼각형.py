N = int(input())

dp = [[0 for _ in range(N)] for _ in range(N)]
arr = []

for _ in range(N):
    tmp_arr = list(map(int, input().split()))
    tmp_arr.insert(0, 0)
    tmp_arr.append(0)
    arr.append(tmp_arr)

for x in range(N - 1):
    for y in range(1, len(arr[x])):
        arr[x + 1][y] += max(arr[x][y - 1], arr[x][y])

print(max(arr[N - 1]))