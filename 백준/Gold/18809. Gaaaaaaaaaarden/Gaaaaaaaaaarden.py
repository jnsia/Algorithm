def bfs(bits, arr):
    global cnt

    # green 1 | red 0
    queue = deque()
    ans = 0
    garden_copy = []

    for line in garden:
        garden_copy.append(line[:])

    for idx in range(G + R):
        if bits[idx]:
            x, y = arr[idx]
            queue.append((x, y, 1))
            garden_copy[x][y] = 1
        else:
            x, y = arr[idx]
            queue.append((x, y, 0))
            garden_copy[x][y] = -1

    while queue:
        x, y, color = queue.popleft()

        if garden_copy[x][y] == float('inf'):
            continue

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M:
                if garden_copy[nx][ny] == 0:
                    if color:
                        garden_copy[nx][ny] = garden_copy[x][y] + 1
                        queue.append((nx, ny, 1))
                    else:
                        garden_copy[nx][ny] = garden_copy[x][y] - 1
                        queue.append((nx, ny, 0))
                else:
                    if color and -garden_copy[nx][ny] == garden_copy[x][y] + 1:
                        ans += 1
                        garden_copy[nx][ny] = float('inf')
                    elif not color and -garden_copy[nx][ny] == garden_copy[x][y] - 1:
                        ans += 1
                        garden_copy[nx][ny] = float('inf')

    if ans > cnt:
        cnt = ans

def bit_mask(idx):
    if sum(bits) == G:
        bits_arr.append(bits[:])
        return

    if idx == G + R:
        return

    bits[idx] = 1
    bit_mask(idx + 1)
    bits[idx] = 0
    bit_mask(idx + 1)


def comb(idx, res):
    if len(res) == G + R:
        comb_arr.append(res)
        return

    if idx == case_num:
        return

    comb(idx + 1, res + [ground[idx]])
    comb(idx + 1, res)


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, G, R = map(int, input().split())
garden = []
ground = []

for n in range(N):
    line = list(map(int, input().split()))

    for m in range(M):
        if line[m] == 2:
            ground.append((n, m))
            line[m] = 0
        elif line[m] == 1:
            line[m] = 0
        else:
            line[m] = float('inf')

    garden.append(line)

case_num = len(ground)
collected = [False] * case_num

comb_arr = []
comb(0, [])

bits_arr = []
bits = [0] * (G + R)
bit_mask(0)

cnt = 0

for arr in comb_arr:
    for bits in bits_arr:
        bfs(bits, arr)

print(cnt)