import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

cur_sum = 0
max_sum = 0

for i in range(N - M + 1):
    if i == 0:
        for j in range(M):
            cur_sum += lst[i + j]

        max_sum = cur_sum
    else:
        cur_sum = cur_sum - lst[i - 1] + lst[i + M - 1]

        if max_sum < cur_sum:
            max_sum = cur_sum

print(max_sum)