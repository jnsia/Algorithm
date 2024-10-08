from collections import deque

import sys
input = sys.stdin.readline

N = int(input())

arr = deque()

for i in range(N):
    n = input().split()
    
    if n[0] == 'push':
        arr.append(n[1])
    elif n[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif n[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif n[0] == 'size':
        print(len(arr))
    elif n[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())