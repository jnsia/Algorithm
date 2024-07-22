def perm(depth, res, visited):
    next_visited = visited[:]

    if depth == M:
        print(*res)
        return
    
    for idx in range(N):
        if visited[idx] == False:
            perm(depth + 1, res + [numbers[idx]], next_visited)
            next_visited[idx] = True


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
perm(0, [], visited)