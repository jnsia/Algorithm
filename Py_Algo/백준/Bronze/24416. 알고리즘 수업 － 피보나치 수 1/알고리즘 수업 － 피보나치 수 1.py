def fibonacci1(n):
    result = [0] * (n + 1)

    result[1] = 1
    result[2] = 1

    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2]

    return result[n]

import sys
input = sys.stdin.readline

N = int(input())

print(fibonacci1(N), N - 2)