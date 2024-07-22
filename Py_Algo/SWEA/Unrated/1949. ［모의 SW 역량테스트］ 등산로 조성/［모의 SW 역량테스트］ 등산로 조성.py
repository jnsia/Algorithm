def dfs(coord, height, length, cut):
    global mx_length

    x, y = coord

    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            if height > mountain[nx][ny]:
                visited[nx][ny] = True
                dfs([nx, ny], mountain[nx][ny], length + 1, cut)
                visited[nx][ny] = False
            else:
                for k in range(1, K + 1):
                    if height > mountain[nx][ny] - k and cut == 0:
                        visited[nx][ny] = True
                        dfs([nx, ny], mountain[nx][ny] - k, length + 1, cut + 1)
                        visited[nx][ny] = False
        
    if length > mx_length:
        mx_length = length


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, K = map(int, input().split())
    mountain = []
    top_num = 0
    top_list = []
    mx_length = 0

    for h in range(N):
        line = list(map(int, input().split()))

        for w in range(N):
            if line[w] > top_num:
                top_list.clear()
                top_num = line[w]
                top_list.append([h, w])
            elif line[w] == top_num:
                top_list.append([h, w])

        mountain.append(line)

    visited = [[False] * N for _ in range(N)]

    for top in top_list:
        visited[top[0]][top[1]] = True
        dfs(top, top_num, 1, 0)
        visited[top[0]][top[1]] = False

    print(mx_length)