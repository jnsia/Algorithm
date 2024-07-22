def binary_search(size, key):
    left = 0
    right = size - 1

    while left <= right:
        mid = (left + right) // 2

        if first[mid] == key:
            return 1
        elif first[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return 0


T = int(input())

for _ in range(T):
    N = int(input())
    first = list(map(int, input().split()))

    first.sort()

    M = int(input())
    second = list(map(int, input().split()))

    for i in range(M):
        print(binary_search(N, second[i]))
