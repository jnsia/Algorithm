import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_dict = {}

for n in range(N):
    S, P = map(str, input().split())
    
    site_dict[S] = P
    
for m in range(M):
    print(site_dict[input().strip()])