from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

answer = [float('inf')] * N

min_list = deque()

for i in range(N):
    if not min_list:
        min_list.append([i, arr[i]])
        answer[i] = min_list[0][1]
        continue
    else:
        if min_list[0][0] + L <= i:
            min_list.popleft()

    while min_list and min_list[-1][1] > arr[i]:
        min_list.pop()

    min_list.append([i, arr[i]])
    answer[i] = min_list[0][1]

print(*answer)