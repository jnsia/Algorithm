def gcm(a, b):
    arr = []
    
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            arr.append(i)
    
    return max(arr)

import sys

input = sys.stdin.readline
S = int(input())

for x in range(S):
    n, m = map(int, input().split())
    
    print(int((n * m) / gcm(n, m)))
    
    