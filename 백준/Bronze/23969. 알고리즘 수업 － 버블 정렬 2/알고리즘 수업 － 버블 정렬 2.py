import sys
input = sys.stdin.readline

A, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
res = [0] * A

for i in range(A - 1):
    for j in range(A - 1):
        if arr[j + 1] < arr[j]:
            cnt += 1
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

            if cnt == K:
                print(*arr)

if K > cnt:
    print(-1)
