import sys
input = sys.stdin.readline

M = int(input())

S = set()

for i in range(M):
    lst = list(map(str, input().split()))
    
    if lst[0] == 'add':
        S.add(int(lst[1]))
    elif lst[0] == 'remove':
        S.discard(int(lst[1]))
    elif lst[0] == 'check':
        print(1) if int(lst[1]) in S else print(0)
    elif lst[0] == 'toggle':
        S.discard(int(lst[1])) if int(lst[1]) in S else S.add(int(lst[1]))
    elif lst[0] == 'all':
        S = set(list(range(1, 21)))
    elif lst[0] == 'empty':
        S.clear()