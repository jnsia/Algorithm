N, M = map(int, input().split())
# N = int(input())

bucket = [0] * N

for x in range(M):
    i, j, k = map(int, input().split())

    for y in range(i - 1, j):
        bucket[y] = k

for z in bucket:
    print(z, end=" ")