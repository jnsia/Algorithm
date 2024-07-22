def bfs(map, start):
    visited = set()
    queue = [start]
    cnt = 0

    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)

        if map[vertex[0]][vertex[1]] == 'X':
            continue
        elif map[vertex[0]][vertex[1]] == 'P':
            cnt += 1

        for z in range(4):
            nx = vertex[0] + dx[z]
            ny = vertex[1] + dy[z]

            if (nx, ny) not in visited and 0 <= nx < N and 0 <= ny < M:
                queue.append((nx, ny))
                visited.add((nx, ny))

    if cnt:
        return cnt
    else:
        return 'TT'

N, M = map(int, input().split())
school = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

I_idx = ()

for n in range(N):
    tmp_arr = list(input())

    if 'I' in tmp_arr:
        I_idx = (n, tmp_arr.index('I'))

    school.append(tmp_arr)

print(bfs(school, I_idx))
