def blank_mid(n):
    if n == 0:
        return '-'

    res = blank_mid(n - 1) + ' ' * 3 ** (n - 1) + blank_mid(n - 1)
    return res

import sys
input = sys.stdin.readline

while True:
    try:
        N = int(input())

        print(blank_mid(N))
    except:
        break
