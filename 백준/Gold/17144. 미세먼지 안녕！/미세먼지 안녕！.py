def circulation(matrix):
    new_matrix = []

    for copy_line in matrix:
        new_matrix.append(copy_line[:])

    new_matrix[above][1] = 0
    new_matrix[below][1] = 0
    # above: 1 / below: 0
    queue = deque()

    queue.append((above, 1, 0, 1))
    queue.append((below, 1, 0, 0))

    while queue:
        x, y, direction, is_above = queue.popleft()

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < R and 0 <= ny < C:
            if matrix[nx][ny] != -1:
                new_matrix[nx][ny] = matrix[x][y]
                queue.append((nx, ny, direction, is_above))
        else:
            if is_above:
                queue.append((x, y, (direction + 1) % 4, is_above))
            else:
                queue.append((x, y, (direction - 1) % 4, is_above))

    return new_matrix

def diffusion(matrix):
    new_matrix = []

    for copy_line in matrix:
        new_matrix.append(copy_line[:])

    for x in range(R):
        for y in range(C):
            if matrix[x][y] > 0:
                diffuse_dust = matrix[x][y] // 5
                diffuse_direction = 0

                for move in range(4):
                    nx = x + dx[move]
                    ny = y + dy[move]

                    if 0 <= nx < R and 0 <= ny < C:
                        if matrix[nx][ny] == -1:
                            continue

                        diffuse_direction += 1
                        new_matrix[nx][ny] += diffuse_dust

                new_matrix[x][y] -= diffuse_dust * diffuse_direction

    new_new_matrix = circulation(new_matrix)

    return new_new_matrix

import sys
input = sys.stdin.readline
from collections import deque


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

R, C, T = map(int, input().split())

above = -1
below = -1

house = []

for r in range(R):
    line = list(map(int, input().split()))

    if below == -1 and line[0] == -1:
        above = r
        below = r + 1

    house.append(line)

for _ in range(T):
    house = diffusion(house)

answer = 0

for r in range(R):
    for c in range(C):
        if house[r][c] > 0:
            answer += house[r][c]

print(answer)