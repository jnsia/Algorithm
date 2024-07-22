def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [child for child in range(N + 1)]
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

for i in range(N):
    for j in range(i, N):
        if adj_matrix[i][j] == 1:
            union(i + 1, j + 1)

is_possible = True
root = find(plan[0])

for city in plan:
    if find(root) != find(city):
        is_possible = False
        break

if is_possible:
    print('YES')
else:
    print('NO')