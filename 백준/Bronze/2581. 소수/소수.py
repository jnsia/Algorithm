def is_prime(n):
    if n == 0 or n == 1:
        return False

    m = int(n ** 0.5)

    result = True

    for i in range(2, m + 1):
        if n % i == 0:
            result = False
            break

    return result

N = int(input())
M = int(input())

arr = []

for i in range(N, M + 1):
    if is_prime(i):
        arr.append(i)


if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)