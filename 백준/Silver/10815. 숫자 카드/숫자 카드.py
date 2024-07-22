import sys

N = int(input())
nNumbers = set(map(int, sys.stdin.readline().split()))
M = int(input())
mNumbers = list(map(int, sys.stdin.readline().split()))

zero = [0 for x in range(M)]

for i in range(M):
    if mNumbers[i] in nNumbers:
        zero[i] = 1
    print(zero[i], end=" ")