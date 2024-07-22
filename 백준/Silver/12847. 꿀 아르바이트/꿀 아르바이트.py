n, m = map(int, input().split())
money = list(map(int, input().split()))

cur_sum = sum(money[0:m])
mx_sum = cur_sum

for idx in range(m, n):
    cur_sum -= money[idx - m]
    cur_sum += money[idx]

    if cur_sum > mx_sum:
        mx_sum = cur_sum

print(mx_sum)