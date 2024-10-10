from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

queue = deque()
# 수량, 질량의 합, 속력의 합, 방향의 합, 방향 % 2의 합
grid = [[[0, 0, 0, 0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    queue.append((r, c, m, s, d))

while K:
    for _ in range(len(queue)):
        r, c, m, s, d = queue.popleft()

        if m == 0:
            continue

        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N

        grid[nr][nc][0] += 1
        grid[nr][nc][1] += m
        grid[nr][nc][2] += s
        grid[nr][nc][3] += d
        grid[nr][nc][4] += d % 2

    for r in range(N):
        for c in range(N):
            n, m, s, d, d2 = grid[r][c]

            if n == 1:
                queue.append((r, c, m, s, d))
            elif n > 1:
                if d2 in [0, n]:
                    queue.append((r, c, m // 5, s // n, 0))
                    queue.append((r, c, m // 5, s // n, 2))
                    queue.append((r, c, m // 5, s // n, 4))
                    queue.append((r, c, m // 5, s // n, 6))
                else:
                    queue.append((r, c, m // 5, s // n, 1))
                    queue.append((r, c, m // 5, s // n, 3))
                    queue.append((r, c, m // 5, s // n, 5))
                    queue.append((r, c, m // 5, s // n, 7))

            grid[r][c] = [0, 0, 0, 0, 0]

    K -= 1

answer = 0

for _ in range(len(queue)):
    r, c, m, s, d = queue.popleft()
    answer += m

print(answer)
