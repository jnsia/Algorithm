import math

def c(a, b):
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

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