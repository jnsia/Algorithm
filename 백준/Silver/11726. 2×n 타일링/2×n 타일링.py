def f(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def c(a, b):
    return f(a) // (f(b) * f(a - b))

import sys
input = sys.stdin.readline

N = int(input())

A = N
B = 0
ans = 0

while A >= B:
    ans += c(A, B)
    A -= 1
    B += 1
    
print(ans % 10007)