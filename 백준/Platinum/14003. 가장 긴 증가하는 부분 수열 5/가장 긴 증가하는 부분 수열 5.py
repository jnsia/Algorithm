from collections import deque


def lower_bound(key):
    low = 1
    high = len(lis) - 1

    while low < high:
        mid = (low + high) // 2

        if lis[mid] >= key:
            high = mid
        else:
            low = mid + 1

    return high


N = int(input())
arr = [0] + list(map(int, input().split()))

lis = [-float('inf')]
path = [-1] * (N + 1)
max_path = 0

for idx in range(1, N + 1):
    num = arr[idx]

    if lis[-1] < num:
        lis.append(num)
        max_path += 1
        path[idx] = max_path
    else:
        low_idx = lower_bound(arr[idx])
        lis[low_idx] = num
        path[idx] = low_idx
        max_path = max(max_path, path[idx])

max_len = len(lis) - 1
print(max_len)

answer = deque()
min_len = 1

for idx in range(N):
    if path[N - idx] == max_len:
        answer.appendleft(arr[N - idx])
        max_len -= 1

print(*answer)
