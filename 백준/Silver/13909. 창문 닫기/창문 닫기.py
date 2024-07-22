import sys

input = sys.stdin.readline

def is_square(n):
    cnt = 0

    for i in range(1, int(n ** 0.5) + 1):
        cnt += 1

    return cnt

N = int(input())

print(is_square(N))
