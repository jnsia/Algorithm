import sys
input = sys.stdin.readline
from collections import deque

def bfs(coord):
    queue = deque()
    queue.append(coord)
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M and passage[nx][ny] == 1:
                passage[nx][ny] = 0
                queue.append([nx, ny])

    return cnt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())
passage = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())

    passage[r-1][c-1] = 1

mx = 0

for i in range(N):
    for j in range(M):
        if passage[i][j] == 1:
            passage[i][j] = 0
            res = bfs([i, j])

            if res > mx:
                mx = res

print(mx)