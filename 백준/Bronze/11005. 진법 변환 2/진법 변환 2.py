sequence = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, input().split())

a = ''

while N > 0:
    a += sequence[N % B]
    N = N // B


print(a[::-1])