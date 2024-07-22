def search(start):
    new_lst = []

    for el in arr[:]:
        new_lst.append(el[:])

    stack = [start]

    while stack:
        vertex = stack.pop()
        x = vertex[0]
        y = vertex[1]

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M and new_lst[nx][ny] > 0:
                stack.append([nx, ny])
                new_lst[nx][ny] = 0

    for a in new_lst:
        for b in a:
            if b > 0:
                return True

    return False


def bfs(start_list):
    queue = deque([*start_list])
    cnt = 1

    while queue:
        new_arr = []
        search_coord = [0, 0]

        for el in arr[:]:
            new_arr.append(el[:])

        for _ in range(len(queue)):
            vertex = queue.popleft()
            x = vertex[0]
            y = vertex[1]

            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                if 0 <= nx < N and 0 <= ny < M and arr[x][y] > 0:
                    if new_arr[nx][ny] == 0:
                        arr[x][y] -= 1

            if arr[x][y] > 0:
                queue.append([x, y])
                search_coord = [x, y]

        if search(search_coord):
            return cnt

        cnt += 1

    return 0

from collections import deque

N, M = map(int, input().split())
arr = []
early = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for n in range(N):
    line = list(map(int, input().split()))

    for m in range(M):
        if line[m] > 0:
            early.append([n, m])

    arr.append(line)


print(bfs(early))
