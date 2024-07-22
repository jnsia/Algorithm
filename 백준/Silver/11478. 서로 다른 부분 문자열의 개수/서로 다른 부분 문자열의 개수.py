import sys

input = sys.stdin.readline
S = input()

one = set()

for x in range(len(S)):
    for y in range(x + 1, len(S)):
        one.add(S[x:y])
        
print(len(one))