def upper_bound(key):
    low = 0
    high = len(right_combs) - 1

    while low <= high:
        mid = (low + high) // 2
        temp = right_combs[mid] + key

        if temp <= C:
            low = mid + 1
        else:
            high = mid - 1

    return high


def comb(depth, max_depth, arr, res, new_arr):
    if depth == max_depth:
        new_arr.append(res)
        return

    comb(depth + 1, max_depth, arr, res, new_arr)
    comb(depth + 1, max_depth, arr, res + arr[depth], new_arr)


N, C = map(int, input().split())
things = list(map(int, input().split()))

mid = N // 2

left_things = things[:mid]
right_things = things[mid:]

left_combs = []
right_combs = []

comb(0, mid, left_things, 0, left_combs)
comb(0, N - mid, right_things, 0, right_combs)

right_combs.sort()

answer = 0

for idx in range(len(left_combs)):
    res = upper_bound(left_combs[idx])
    answer += res + 1

print(answer)