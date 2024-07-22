def hanoi(first, second, third, n):
    if n == 1:
        pass
    elif n == 2:
        print(first, second)
        print(first, third)
        print(second, third)
    else:
        hanoi(first, third, second, n - 1)
        print(first, third)
        hanoi(second, first, third, n - 1)

import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 20

dp[0] = 1

for i in range(1, 20):
    dp[i] = dp[i - 1] * 2 + 1

if T == 1:
    print(1)
    print(1, 3)
else:
    print(dp[T - 1])
    hanoi(1, 2, 3, T)