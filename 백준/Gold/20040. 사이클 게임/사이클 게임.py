def find(elem):
    if parent[elem] == elem:
        return elem

    parent[elem] = find(parent[elem])
    return parent[elem]

def union(elem1, elem2):
    elem1 = find(elem1)
    elem2 = find(elem2)

    if elem1 > elem2:
        parent[elem1] = elem2
    else:
        parent[elem2] = elem1


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [child for child in range(N)]
answer = 0

for idx in range(1, M + 1):
    dot1, dot2 = map(int, input().split())

    if find(dot1) == find(dot2):
        if not answer:
            answer = idx
    else:
        union(dot1, dot2)

print(answer)