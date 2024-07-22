import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.insert(0, 0)
lst.insert(0, 0)

for i in range(1, N + 2):
    lst[i] += lst[i - 1]

for _ in range(M):
    a, b = map(int, input().split())

    print(lst[b + 1] - lst[a])