def perm(depth, res):
    if depth == M:
        print(*res)
        return
    
    for num in visited.keys():
        if visited[num] > 0:
            visited[num] -= 1
            perm(depth + 1, res + [num])
            visited[num] += 1


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = dict()

for num in numbers:
    visited.setdefault(num, 0)
    visited[num] += 1

perm(0, [])