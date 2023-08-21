import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

min_sum = 0

for idx in range(N):
    min_sum += A[idx] * B[idx]

print(min_sum)