arr = list(map(int, input().split()))

num = min(arr)

while True:
    res = 0

    for i in range(5):
        if num % arr[i] == 0:
            res += 1

    if res >= 3:
        break

    num += 1

print(num)