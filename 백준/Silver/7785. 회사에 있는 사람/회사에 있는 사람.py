import sys

N = int(sys.stdin.readline())

company = {}

for i in range(N):
    P, C = map(str, sys.stdin.readline().split())
    
    if C == 'enter':
        company[P] = True
    elif C == 'leave':
        company[P] = False
        
arr = [k for k, v in company.items() if v == True]
arr.sort(reverse=True)
print(*arr, sep="\n")