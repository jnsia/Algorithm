import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    n = sys.stdin.readline().split()
    
    if n[0] == 'push':
        arr.append(n[1])
    elif n[0] == 'top':
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
            print(arr.pop())