def dfs(res):
    for i in range(res % 10):
        dfs(res * 10 + i)

    arr.append(res)

N = int(input())
arr = []
for i in range(10):
    dfs(i)
arr.sort()
if N >= len(arr):
    print(-1)
else:
    print(arr[N])