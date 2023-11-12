def lower_bound(key):
    low = 0
    high = len(right_comb) - 1

    while low <= high:
        mid = (low + high) // 2
        sum_value = key + right_comb[mid]

        if sum_value >= S:
            high = mid - 1
        else:
            low = mid + 1

    return low


def upper_bound(key):
    low = 0
    high = len(right_comb) - 1

    while low <= high:
        mid = (low + high) // 2
        sum_value = key + right_comb[mid]

        if sum_value <= S:
            low = mid + 1
        else:
            high = mid - 1

    return high


def comb(idx, end, dirt, res):
    if idx == end:
        if dirt == 0:
            left_comb.append(res)
        else:
            right_comb.append(res)
        return

    if dirt == 0:
        comb(idx + 1, end, dirt, res)
        comb(idx + 1, end, dirt, res + left_arr[idx])
    else:
        comb(idx + 1, end, dirt, res)
        comb(idx + 1, end, dirt, res + right_arr[idx])


N, S = map(int, input().split())
arr = list(map(int, input().split()))

mid = N // 2

left_arr = arr[:mid]
right_arr = arr[mid:]

left_comb = []
right_comb = []

comb(0, mid, 0, 0)
comb(0, N - mid, 1, 0)

right_comb.sort()

answer = 0

# print(left_comb)
# print(right_comb)

for elem in left_comb:
    low_idx = lower_bound(elem)
    high_idx = upper_bound(elem)

    # print(low_idx, high_idx, '---')
    # print(elem, right_comb[low_idx], right_comb[high_idx])

    if elem + right_comb[high_idx] == S:
        answer += high_idx - low_idx + 1

if S == 0:
    print(answer - 1)
else:
    print(answer)