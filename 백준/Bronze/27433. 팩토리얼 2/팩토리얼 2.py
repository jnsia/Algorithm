def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

import sys
input = sys.stdin.readline

N = int(input())

print(factorial(N))