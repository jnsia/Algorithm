import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

min_key = 1
max_key = 20000000001

res = 0

while max_key >= min_key:
    half_key = (max_key + min_key) // 2
    sum_height = 0

    for i in trees:
        if half_key < i:
            sum_height += i - half_key

    if sum_height >= M:
        min_key = half_key + 1

        if res <= half_key:
            res = half_key

    elif sum_height < M:
        max_key = half_key - 1

print(res)