def pibopibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return pibopibo(n - 1) + pibopibo(n - 2)

import sys
input = sys.stdin.readline

N = int(input())

print(pibopibo(N))