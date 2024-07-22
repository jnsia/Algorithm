import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end, init):
    queue = deque([[start, init]])

    while queue:
        num, cnt = queue.popleft()

        if num > end:
            continue

        if num == end:
            print(cnt)
            return

        if num * 2 < 1000000001:
            queue.append([num * 2, cnt + 1])

        if num * 10 + 1 < 1000000001:
            queue.append([num * 10 + 1, cnt + 1])
    
    print(-1)


A, B = map(int, input().split())

bfs(A, B, 1)