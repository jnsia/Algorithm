def bfs(start):
    queue = start
    time = 0

    while queue:
        queue.sort(key=lambda x: x[2], reverse=True)
        time += 1

        for _ in range(len(queue)):
            x, y, life, active = queue.pop(0)

            if active > 0:
                queue.append([x, y, life, active - 1])
                continue
            elif active == 0 and life > 1:
                queue.append([x, y, 0, life - 2])

            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append([nx, ny, life, life])

        if time == K:
            print(len(queue))
            break


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, M, K = map(int, input().split())
    visited = set()

    start = []

    for i in range(N):
        line = list(map(int, input().split()))

        for j in range(M):
            if line[j] > 0:
                visited.add((i, j))
                start.append([i, j, line[j], line[j]])

    bfs(start)