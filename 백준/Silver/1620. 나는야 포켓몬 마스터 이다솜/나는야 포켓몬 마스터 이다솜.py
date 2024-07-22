import sys

N, M = map(int, sys.stdin.readline().split())

pocketmon = dict()
pocketmon2 = dict()

for i in range(1, N + 1):
    n = sys.stdin.readline().strip()
    pocketmon[str(i)] = n
    pocketmon2[n] = str(i)
    
for j in range(M):
    question = sys.stdin.readline().strip()
    
    if question.isdecimal():
        print(pocketmon[question])
    else:
        print(pocketmon2[question])