import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    n, m = map(int, sys.stdin.readline().split())
    arr.append((n, m))

arr.sort(key=lambda x: x[1])
arr.sort(key=lambda x: x[0])

for j in range(N):
    print(*arr[j])