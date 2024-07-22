def is_han(num):
    if num == 1000:
        return False

    arr = [0, 0, 0]
    size = 0

    while num > 0:
        arr[size] = num % 10
        num //= 10
        size += 1

    if size < 3:
        return True
    else:
        diff = arr[1] - arr[0]

        if diff == arr[2] - arr[1]:
            return True
        else:
            return False


N = int(input())

answer = 0

for i in range(1, N + 1):
    if is_han(i):
        answer += 1

print(answer)