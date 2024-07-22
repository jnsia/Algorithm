def dfs(matrix, color, x, y):
    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == color:
            matrix[nx][ny] = 'W'
            dfs(matrix, color, nx, ny)


import sys
sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
grid = [list(input()) for _ in range(N)]

normal = [line[:] for line in grid]
abnormal = []

for line in grid:
    tmp_line = []
    
    for color in line[:]:
        if color == 'G':
            tmp_line.append('R')
        else:
            tmp_line.append(color)
    
    abnormal.append(tmp_line)

normal_cnt = 0
abnormal_cnt = 0

for i in range(N):
    for j in range(N):
        if normal[i][j] != 'W':
            normal_cnt += 1
            dfs(normal, normal[i][j], i, j)

        if abnormal[i][j] != 'W':
            abnormal_cnt += 1
            dfs(abnormal, abnormal[i][j], i, j)

print(normal_cnt, abnormal_cnt)