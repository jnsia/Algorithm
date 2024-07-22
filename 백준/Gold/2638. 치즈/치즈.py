def bfs(start):
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = [start]
    cur_cheese = []

    for line in cheese[:]:
        cur_cheese.append(line[:])

    while queue:
        vertex = queue.pop()
        x = vertex[0]
        y = vertex[1]
        visited[x][y] = True

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if cur_cheese[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                elif cur_cheese[nx][ny] == 1 and cheese[nx][ny] > 0:
                    cheese[nx][ny] -= 0.5


from pprint import pprint as print

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
cheese = []

for _ in range(N):
    line = list(map(int, input().split()))
    cheese.append(line)

hour = 0

while True:
    left_cheese_num = 0


    for i in range(N):
        for j in range(M):
            if cheese[i][j] > 0:
                cheese[i][j] = 1

            if cheese[i][j] == 1:
                left_cheese_num += 1

    bfs([0, 0])

    if left_cheese_num == 0:
        break
    
    hour += 1

print(hour)