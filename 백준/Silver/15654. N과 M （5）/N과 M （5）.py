def perm(depth, res):
    if depth == M:
        print(*res)
        return
    
    for idx in range(N):
        if visited[idx] == False:
            visited[idx] = True
            perm(depth + 1, res + [numbers[idx]])
            visited[idx] = False

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
perm(0, [])