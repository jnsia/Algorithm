import sys

N, M = map(int, sys.stdin.readline().split())

N_set = set()

for i in range(N):
    N_set.add(sys.stdin.readline())
    
cnt = 0
    
for j in range(M):
    if sys.stdin.readline() in N_set:
        cnt += 1
        
print(cnt)