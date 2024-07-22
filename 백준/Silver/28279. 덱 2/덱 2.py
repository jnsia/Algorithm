from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque()

for n in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        arr.appendleft(command[1])
    elif command[0] == 2:
        arr.append(command[1])
    elif command[0] == 3:
        if arr:
            temp = arr.popleft()
            print(temp)
        else:
            print(-1)
    elif command[0] == 4:
        if arr:
            temp = arr.pop()
            print(temp)
        else:
            print(-1)
    elif command[0] == 5:
        print(len(arr))
    elif command[0] == 6:
        if arr:
            print(0)
        else:
            print(1)
    elif command[0] == 7:
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif command[0] == 8:
        if arr:
            print(arr[-1])
        else:
            print(-1)
