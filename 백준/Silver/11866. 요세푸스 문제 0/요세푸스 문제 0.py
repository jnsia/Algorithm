import sys

N, M = map(int, sys.stdin.readline().split())

arr = [x for x in range(1, N + 1)]
arr2 = []

index = 0
print('<', end="")

for i in range(N):
    index += M - 1

    while index >= len(arr):
        index -= len(arr)
    
    temp = arr.pop(index)
    arr2.append(temp)

print(*arr2, sep=", ", end="")
print('>', end="")
