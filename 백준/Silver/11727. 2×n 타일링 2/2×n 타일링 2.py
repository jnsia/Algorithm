import math
import sys

def combination(a, b):
    if b == 0:
        return 1
    
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

input = sys.stdin.readline

N = int(input())

# nC0 + 2 * n-1C1 + 4 * n-2C2

A = N
B = 0

res = 0

for i in range(N):
    if A < B:
        break

    res += combination(A, B) * (2 ** i)
    A -= 1
    B += 1

print(res % 10007)