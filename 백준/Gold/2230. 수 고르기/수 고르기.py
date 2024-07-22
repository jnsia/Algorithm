N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

answer = 2000000001

j = 1

for i in range(N - 1):
    j = max(j, i + 1)

    res = abs(arr[j] - arr[i])

    while j < N - 1 and res < M:
        j += 1
        res = abs(arr[j] - arr[i])

    if res >= M:
        answer = min(answer, res)

print(answer)