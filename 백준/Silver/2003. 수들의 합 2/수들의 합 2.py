N, M = map(int, input().split())
numbers = list(map(int, input().split()))

i = 0
j = 0
cnt = 0
cur_sum = numbers[0]

while i < N:
    if cur_sum == M:
        cnt +=1

        if j < N - 1:
            j += 1
            cur_sum += numbers[j]
        else:
            cur_sum -= numbers[i]
            i += 1
        # print(cur_sum, i, j)
    elif cur_sum < M and j < N - 1:
        if j < N - 1:
            j += 1
            cur_sum += numbers[j]
        else:
            cur_sum -= numbers[i]
            i += 1
        # print(cur_sum, i, j)
    else:
        cur_sum -= numbers[i]
        i += 1
        # print(cur_sum, i, j)

print(cnt)