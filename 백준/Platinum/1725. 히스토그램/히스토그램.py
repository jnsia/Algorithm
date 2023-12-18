def solve(s, e):
    if s == e:
        return 0

    if s + 1 == e:
        return arr[s]

    mid = (s + e) // 2

    mid_height = arr[mid]
    mid_width = 1
    max_value = mid_width * mid_height

    left = mid
    right = mid

    while left >= s and right < e:
        left_height = -1
        right_height = -1

        if left > s:
            left_height = arr[left - 1]

        if right < e - 1:
            right_height = arr[right + 1]

        if left_height > right_height:
            left -= 1
            mid_height = min(mid_height, left_height)
        else:
            right += 1
            mid_height = min(mid_height, right_height)

        mid_width += 1
        max_value = max(max_value, mid_width * mid_height)

    while left > s:
        left -= 1
        left_height = arr[left]
        mid_height = min(mid_height, left_height)
        mid_width += 1
        max_value = max(max_value, mid_width * mid_height)

    while right < e - 1:
        right += 1
        right_height = arr[right]
        mid_height = min(mid_height, right_height)
        mid_width += 1
        max_value = max(max_value, mid_width * mid_height)

        print(max_value)

    return max(solve(s, mid), solve(mid, e), max_value)


import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

print(solve(0, N))