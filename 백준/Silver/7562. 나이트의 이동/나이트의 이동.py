def bfs(start, end):
    dp = [[0] * L for _ in range(L)]
    queue = deque([start])
    dp[start[0]][start[1]] = 0

    while True:
        coord = queue.popleft()
        x = coord[0]
        y = coord[1]        

        for move in range(8):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < L and 0 <= ny < L and dp[nx][ny] == 0:
                dp[nx][ny] = dp[x][y] + 1
                queue.append([nx, ny])

        if x == end[0] and y == end[1]:
            return dp[x][y]

from collections import deque

T = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

for tc in range(T):
    L = int(input())
    current = list(map(int, input().split()))
    destination = list(map(int, input().split()))

    print(bfs(current, destination))