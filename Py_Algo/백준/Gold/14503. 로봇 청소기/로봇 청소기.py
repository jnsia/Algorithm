def bfs(sx, sy, sz):
    cleaned = [[False for _ in range(M)] for _ in range(N)]
    queue = [[sx, sy, sz]]
    clean_num = 0

    while queue:
        x, y, z = queue.pop(0)

        if cleaned[x][y] == False:
            cleaned[x][y] = True
            clean_num += 1

        is_cleaned = True

        for move in range(3, -1, -1):
            nx = x + dx[(move + z) % 4]
            ny = y + dy[(move + z) % 4]
            nz = (move + z) % 4

            if cleaned[nx][ny] == False and room[nx][ny] == 0:
                is_cleaned = False
                queue.append([nx, ny, nz])
                break

        if is_cleaned:
            bx = x + dx[(z + 2) % 4]
            by = y + dy[(z + 2) % 4]

            if room[bx][by] == 0:
                queue.append([bx, by, z])

    print(clean_num)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

bfs(r, c, direction)