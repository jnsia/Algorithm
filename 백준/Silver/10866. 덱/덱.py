import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    n = sys.stdin.readline().split()
    
    if n[0] == 'push_back':
        arr.append(n[1])
    elif n[0] == 'push_front':
        arr.insert(0, n[1])
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
    elif n[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    elif n[0] == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())