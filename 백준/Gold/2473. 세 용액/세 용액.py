def binary_search(low, high, key):
    opt = 1000000001
    res = -1

    while low <= high:
        mid = (low + high) // 2
        mix = key + arr[mid]

        if abs(opt) > abs(mix):
            opt = mix
            res = mid

        if mix == 0:
            return mid
        elif mix > 0:
            high = mid - 1
        else:
            low = mid + 1

    return res


N = int(input())
arr = sorted(list(map(int, input().split())))

opt_three = 3000000001
answer = (-1, -1, -1)

for i in range(N - 2):
    j = i + 1
    k = N - 1

    while j < k:
        three = arr[i] + arr[j] + arr[k]

        if abs(opt_three) > abs(three):
            opt_three = three
            answer = (arr[i], arr[j], arr[k])

        if three > 0:
            k -= 1
        elif three < 0:
            j += 1
        else:
            break

print(*answer)