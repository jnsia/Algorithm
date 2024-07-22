def dfs(x, y, res):
    global mx

    if res == 26 or mx == 26:
        mx = 26
        return

    if res > mx:
        mx = res

    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < R and 0 <= ny < C:
            word = plane[nx][ny]

            if alphabet[word] == 0:
                alphabet[word] = 1
                dfs(nx, ny, res + 1)
                alphabet[word] = 0


import sys
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

R, C = map(int, input().split())
mx = 0

plane = [[0] * C for _ in range(R)]

ord_A = ord('A')

for r in range(R):
    line = list(input().rstrip())

    for c in range(C):
        plane[r][c] = ord(line[c]) - ord_A

alphabet = [0] * 26
alphabet[plane[0][0]] = 1

dfs(0, 0, 1)

print(mx)