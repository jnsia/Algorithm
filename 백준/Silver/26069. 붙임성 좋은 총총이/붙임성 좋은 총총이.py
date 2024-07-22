import sys

input = sys.stdin.readline

N = int(input())

dance = set()
contact_dict = dict()

dance.add('ChongChong')

for i in range(N):
    n, m = input().split()
    
    if n in dance:
        dance.add(m)
    elif m in dance:
        dance.add(n)

print(len(dance))