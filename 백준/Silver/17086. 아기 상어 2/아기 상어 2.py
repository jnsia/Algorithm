dx = [1, 0, -1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

N, M = map(int, input().split())
matrix = []
shark = []
mx_safe = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            shark.append((i, j))
    matrix.append(line)

while shark:
    x, y = shark.pop(0)

    for move in range(8):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            shark.append((nx, ny))

            next_safe = matrix[nx][ny]

            if next_safe > mx_safe:
                mx_safe = next_safe

print(mx_safe - 1)