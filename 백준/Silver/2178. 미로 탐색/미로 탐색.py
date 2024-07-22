def bfs(start):
    queue = deque([start])
    cnt = -1

    while queue:
        if plane[N - 1][M - 1] == 0:
            return cnt

        cnt += 1

        for _ in range(len(queue)):
            vertex = queue.popleft()
            x = vertex[0]
            y = vertex[1]


            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                if 0 <= nx < N and 0 <= ny < M and plane[nx][ny] == 1:
                    queue.append([nx, ny])
                    plane[nx][ny] = 0




from collections import deque

N, M = map(int, input().split())
plane = [list(map(int, list(input()))) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

res_cnt = bfs([0, 0])
print(res_cnt + 2)

