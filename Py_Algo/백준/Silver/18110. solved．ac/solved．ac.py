import sys
from collections import deque

def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

N = int(sys.stdin.readline())

n = round(N * 0.15)
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
arr = deque(arr)

for _ in range(n):
    arr.popleft()
    arr.pop()
    
if len(arr) != 0:
    a = round(sum(arr) / len(arr))
    print(a)
else:
    print(0)
    