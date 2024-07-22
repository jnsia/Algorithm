def restrict(plane, i, j):
    res_plane = []

    for line in plane:
        res_plane.append(line[:])

    for move in range(3):
        for times in range(N - i):
            ni = i + di[move] * times
            nj = j + dj[move] * times

            if 0 <= ni < N and 0 <= nj < N and res_plane[ni][nj] == 0:
                res_plane[ni][nj] = 1

    return res_plane


def dfs(a, b, plane):
    global cnt

    new_plane = restrict(plane, a, b)

    if a == N - 1:
        cnt += 1

    for width in range(N):
        if a < N - 1 and new_plane[a + 1][width] == 0:
            dfs(a + 1, width, new_plane)


di = [1, 1, 1]
dj = [0, -1, 1]

N = int(input())
chess = [[0] * N for _ in range(N)]
cnt = 0

for x in range(N):
    dfs(0, x, chess)

print(cnt)