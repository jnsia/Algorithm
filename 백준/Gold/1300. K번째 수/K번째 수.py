def upper_bound():
    low = 1
    high = K
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        temp = 0

        for i in range(1, N + 1):
            temp += min(mid // i, N)
            # print(mid, temp)

        # print('-----')

        if temp >= K:
            high = mid - 1
            answer = mid
        else:
            low = mid + 1

    return answer


N = int(input())
K = int(input())

sqr_list = [0] * 100001
answer = upper_bound()
print(answer)