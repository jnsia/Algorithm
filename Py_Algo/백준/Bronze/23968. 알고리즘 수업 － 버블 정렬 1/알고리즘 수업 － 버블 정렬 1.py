import sys
input = sys.stdin.readline

A, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 1
res = [0, 0]

for i in range(A):
    for j in range(A - 1):
        if arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

            if cnt == K:
                res = [arr[j], arr[j + 1]]

            cnt += 1

if K < cnt:
    print(*res)
else:
    print(-1)