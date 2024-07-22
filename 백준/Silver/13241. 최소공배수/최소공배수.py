def gcm(a, b):
    gcm_num = 0
    
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcm_num = i
    
    return gcm_num

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

print(int((n * m) / gcm(n, m)))
