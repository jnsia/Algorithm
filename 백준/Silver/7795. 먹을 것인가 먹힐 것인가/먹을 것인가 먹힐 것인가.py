def binary_search(key):
    low = 0
    high = M - 1

    result = -1

    while low <= high:
        mid = (low + high) // 2

        if B[mid] == key:
            high = mid - 1
        elif B[mid] < key:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()

    answer = 0

    for i in range(N):
        result = binary_search(A[i])

        if result != -1:
            answer += result + 1

    print(answer)