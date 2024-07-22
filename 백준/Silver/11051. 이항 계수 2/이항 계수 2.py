def div_square(a, b, c):
    if b == 0:
        return 1

    res = div_square(a, b // 2, c) % c

    if b % 2 == 0:
        return res * res % c
    else:
        return res * res * a % c


def factorial(num, p):
    res = 1

    for i in range(2, num + 1):
        res *= i
        res %= p

    return res


A, B = map(int, input().split())

p = 10007
C = factorial(A, p) * div_square(factorial(B, p) * factorial(A - B, p), p - 2, p)
print(C % p)
