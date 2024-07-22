def lower_bound(key):
    low = 1
    high = len(electric_line) - 1

    while low <= high:
        mid = (low + high) // 2

        if electric_line[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return low


N = int(input())
arr = [(0, 0)]
electric_line = [-1]
path = [-1] * (N + 1)

for _ in range(N):
    A, B = map(int, input().split())
    arr.append((A, B))

arr.sort(key=lambda k: k[0])
ans = []

for idx in range(1, N + 1):
    start, end = arr[idx]
    low_idx = lower_bound(end)

    if electric_line[-1] < end:
        electric_line.append(end)
        ans.append([len(electric_line) - 1, start, end])
    else:
        ans.append([low_idx, start, end])
        electric_line[low_idx] = end

print(N - len(electric_line) + 1)

up_up_up = len(electric_line) - 1

answer = []

for idx in range(len(ans) - 1, -1, -1):
    ans_idx, ans_start, ans_end = ans[idx]

    if ans_idx == up_up_up:
        up_up_up -= 1
    else:
        answer.append(ans_start)

for start in sorted(answer):
    print(start)
