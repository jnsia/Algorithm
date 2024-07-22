def bfs(start, matrix):
    queue = start

    while queue:
        x, y = queue.pop(0)

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                queue.append([nx, ny])


    safety_area = 0

    for h in range(N):
        for w in range(M):
            if matrix[h][w] == 0:
                safety_area += 1

    return safety_area


def dfs(wall_num, matrix):
    global mx_safe

    copy_matrix = []

    for line in matrix:
        copy_matrix.append(line[:])

    if wall_num == 3:
        a = bfs(virus[:], copy_matrix)

        if mx_safe < a:
            mx_safe = a
        
        return
    
    for i in range(N):
        for j in range(M):
            if copy_matrix[i][j] == 0:
                copy_matrix[i][j] = 1
                dfs(wall_num + 1, copy_matrix)
                copy_matrix[i][j] = 0


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
lab = []
virus = []
mx_safe = 0

for n in range(N):
    line = list(map(int, input().split()))

    for m in range(M):
        if line[m] == 2:
            virus.append([n, m])

    lab.append(line)

dfs(0, lab)
print(mx_safe)