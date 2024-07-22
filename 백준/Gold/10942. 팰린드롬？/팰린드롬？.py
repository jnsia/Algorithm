import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

counting = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    counting[i][i] = 1

for i in range(1, N):
    if arr[i] == arr[i + 1]:
        counting[i][i + 1] = 1

for diff in range(2, N):
    for i in range(1, N + 1 - diff):
        if arr[i] == arr[i + diff] and counting[i + 1][i + diff - 1]:
            counting[i][i + diff] = 1

M = int(input())

for _ in range(M):
    s, e = map(int, input().split())
    print(counting[s][e])