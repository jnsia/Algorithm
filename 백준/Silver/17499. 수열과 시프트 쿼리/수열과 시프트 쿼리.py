import sys
input = sys.stdin.readline

from collections import deque

N, Q = map(int, input().split())
A = deque(list(map(int, input().split())))

pointer = 0

for _ in range(Q):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        A[(pointer + (cmd[1] - 1)) % N] += cmd[2]
    
    if cmd[0] == 2:
        pointer -= cmd[1]
    
    if cmd[0] == 3:
        pointer += cmd[1]
        
for idx in range(N):
    print(A[(idx + pointer) % N], end=" ")