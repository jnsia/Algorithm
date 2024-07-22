def bfs(start, end):
    queue = deque([start])
    ez, ex, ey = end
    time = 0

    while queue:
        for _ in range(len(queue)):
            z, x, y = queue.popleft()

            if z == ez and x == ex and y == ey:
                print(f'Escaped in {time} minute(s).')
                return

            for move in range(6):
                nz = z + dz[move]
                nx = x + dx[move]
                ny = y + dy[move]

                if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                    if building[nz][nx][ny] == '.':
                        building[nz][nx][ny] = '#'
                        queue.append([nz, nx, ny])

        time += 1

    print('Trapped!')


import sys
input = sys.stdin.readline
from collections import deque

dz = [1, 0, 0, -1, 0, 0]
dx = [0, 1, 0, 0, -1, 0]
dy = [0, 0, 1, 0, 0, -1]

while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    building = []

    # 층, 세로, 가로
    sz, sx, sy = -1, -1, -1
    ez, ex, ey = -1, -1, -1

    for l in range(L):
        plane = []

        for r in range(R):
            line = list(input())

            # 한 줄 한 줄 검사해보기
            for c in range(C):
                if line[c] == 'S':
                    line[c] = '#'
                    sz, sx, sy = l, r, c

                if line[c] == 'E':
                    line[c] = '.'
                    ez, ex, ey = l, r, c

            #
            plane.append(line)

        # 빌딩을 한 층씩 쌓
        building.append(plane)
        # 쓸모없는 공백 제거
        blank = input()

    bfs([sz, sx, sy], [ez, ex, ey])