import sys

input = sys.stdin.readline
N, M = map(int, input().split())

one = set()
two = set()

for i in range(N):
    one.add(input().rstrip())
    
for j in range(M):
    two.add(input().rstrip())
    
three = list(one & two)
three.sort()
print(len(three), *three, sep='\n')
