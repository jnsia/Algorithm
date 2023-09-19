def merge_sort(low, high):
    global check

    if low < high:
        mid = (low + high) // 2

        merge_sort(low, mid)
        merge_sort(mid + 1, high)

        merged_lst = []
        left_idx = low
        right_idx = mid + 1

        while left_idx <= mid and right_idx <= high:
            if A[left_idx] <= A[right_idx]:
                merged_lst.append(A[left_idx])
                left_idx += 1
            else:
                merged_lst.append(A[right_idx])
                right_idx += 1

        while left_idx <= mid:
            merged_lst.append(A[left_idx])
            left_idx += 1

        while right_idx <= high:
            merged_lst.append(A[right_idx])
            right_idx += 1

        for idx in range(len(merged_lst)):
            A[low + idx] = merged_lst[idx]

            while check < N and A[check] == B[check]:
                check += 1

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
check = 0
is_same = 0

if A == B:
    is_same = 1
else:
    merge_sort(0, N - 1)

if check == N:
    is_same = 1

print(is_same)