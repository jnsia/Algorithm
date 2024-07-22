def bin_search(start, end, key):
    low = start
    high = end
    answer = 0

    while low < high:
        mid = (low + high) // 2

        tmp_sum = 0

        for i in budget:
            if i >= mid:
                tmp_sum += mid
            else:
                tmp_sum += i

        # print(tmp_sum)

        if tmp_sum <= key:
            low = mid + 1
            answer = mid
        else:
            high = mid

    return answer


N = int(input())
budget = list(map(int, input().split()))
K = int(input())

if sum(budget) <= K:
    print(max(budget))
else:
    print(bin_search(1, max(budget), K))