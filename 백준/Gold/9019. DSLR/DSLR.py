import sys
input = sys.stdin.readline
from collections import deque

def cmd_D(num):
    return (num * 2) % 10000

def cmd_S(num):
    if num == 0:
        return 9999
    else:
        return num - 1

def cmd_L(num):
    return (num % 1000) * 10 + num // 1000

def cmd_R(num):
    return (num % 10) * 1000 + num // 10

def bfs(start, end, res):
    visited = [False] * 10000
    queue = deque([[start, res]])

    while queue:
        n, r = queue.popleft()

        if n == end:
            print(r)
            return

        D = cmd_D(n)
        S = cmd_S(n)
        L = cmd_L(n)
        R = cmd_R(n)

        if not visited[D]:
            visited[D] = True
            queue.append([D, r + 'D'])

        if not visited[S]:
            visited[S] = True
            queue.append([S, r + 'S'])

        if not visited[L]:
            visited[L] = True
            queue.append([L, r + 'L'])

        if not visited[R]:
            visited[R] = True
            queue.append([R, r + 'R'])


T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())

    bfs(A, B, '')