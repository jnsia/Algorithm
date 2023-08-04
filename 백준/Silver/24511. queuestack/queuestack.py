import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

res = deque()

for i in range(1, N + 1):
    if not A[N - i]:
        res.append(B[N - i])

for k in range(M):
    res.append(C[k])
    print(res[k], end=" ")
    