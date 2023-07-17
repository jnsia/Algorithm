import sys

N = int(input())
A = []

count = [0] * (10001)

for x in range(N):
    n = int(sys.stdin.readline())
    count[n] += 1
    
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)