import sys

def is_prime(n):
    result = True
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if n % i == 0:
            result = False
            break

    return result

T = int(input())

for t in range(T):
    n = int(sys.stdin.readline())

    while True:
        if n == 0 or n == 1:
            n += 1
            continue

        if is_prime(n):
            print(n)
            break

        n += 1