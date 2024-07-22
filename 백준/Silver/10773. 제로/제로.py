import sys

K = int(sys.stdin.readline())

arr = []

for k in range(K):
    n = int(sys.stdin.readline())

    if n != 0:
        arr.append(n)
    else:
        arr.pop()

print(sum(arr))