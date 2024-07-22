def binary_search(key):
    low = 0
    high = N - 1
    close = 2000001

    while low <= high:
        mid = (low + high) // 2
        close = min(close, abs(black_hole[mid] - key))

        if black_hole[mid] == key:
            return 0
        elif black_hole[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return close

N, M = map(int, input().split())

black_hole = list(map(int, input().split()))
black_hole.sort()

P = 0

for _ in range(M):
    location, weight = map(int, input().split())

    close_dist = binary_search(location)
    force = close_dist * weight

    if force > P:
        P = force

print(P)