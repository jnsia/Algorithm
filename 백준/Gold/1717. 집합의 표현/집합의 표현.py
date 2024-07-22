def union(parent, child):
    parent = find(parent)
    child = find(child)

    if parent < child:
        super_shy[child] = parent
    else:
        super_shy[parent] = child

def find(node):
    if super_shy[node] == node:
        return node
    
    if super_shy[node] != node:
        super_shy[node] = find(super_shy[node])

    return super_shy[node]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
super_shy = [x for x in range(N + 1)]

for _ in range(M):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')