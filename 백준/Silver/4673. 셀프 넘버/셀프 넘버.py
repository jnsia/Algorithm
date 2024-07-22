is_self = [True] * 10001

for num in range(1, 10001):
    next_num = num
    temp = num

    while temp > 0:
        next_num += temp % 10
        temp //= 10

    if next_num <= 10000:
        is_self[next_num] = False

for num in range(1, 10001):
    if is_self[num]:
        print(num)