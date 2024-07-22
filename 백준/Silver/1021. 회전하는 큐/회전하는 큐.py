from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

arr = deque(range(1, N + 1))
cnt = 0

for i in range(M):
    while True:
        if arr[0] == lst[i]:
            arr.popleft()
            break
        elif arr.index(lst[i]) > (len(arr) // 2):
            temp = arr.pop()
            arr.appendleft(temp)
            cnt += 1
        elif arr.index(lst[i]) <= (len(arr) // 2):
            temp = arr.popleft()
            arr.append(temp)
            cnt += 1

print(cnt)