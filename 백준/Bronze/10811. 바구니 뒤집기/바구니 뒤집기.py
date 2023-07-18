N, M = map(int, input().split())

bucket = [i for i in range(1, N + 1)]

for x in range(M):
    i, j = map(int, input().split())

    reverse_bucket = bucket[i -1 : j]
    reverse_bucket = reverse_bucket[::-1]

    for z in range(i - 1, j):
        bucket[z] = reverse_bucket[z - i + 1]

for y in bucket:
    print(y, end=" ")