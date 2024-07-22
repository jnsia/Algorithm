def div_square(a, b, c):
    if b == 0:
        return 1

    res = div_square(a, b // 2, c) % c

    if b % 2 == 0:
        return res * res % c
    else:
        return res * res % c * a % c


A, B, C = map(int, input().split())

print(div_square(A % C, B, C))
