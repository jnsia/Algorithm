def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = (len(lst) + 1) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    merged_lst = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_lst.append(left[left_index])
            res.append(left[left_index])
            left_index += 1
        else:
            merged_lst.append(right[right_index])
            res.append(right[right_index])
            right_index += 1

    while left_index < len(left):    
        merged_lst.append(left[left_index])
        res.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged_lst.append(right[right_index])
        res.append(right[right_index])
        right_index += 1

    return merged_lst

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

res = []
merge_sort(A)

if len(res) >= K:
    print(res[K - 1])
else:
    print(-1)