def dfs(x, y, res):
    global mx

    # 12 sec
    # pass

    # 1 sec
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

            # 12 sec
            # if alphabet[word]:
            #     alphabet[word] -= 1
            #     dfs(nx, ny, res + 1)
            #     alphabet[word] += 1

            # 11 sec
            if word not in alphabet:
                alphabet.add(word)
                dfs(nx, ny, res + 1)
                alphabet.remove(word)

import sys
input = sys.stdin.readline
# import time

# 12 sec
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# 10 sec
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# start = time.time()

R, C = map(int, input().split())
mx = 0

# 14 sec
# plane = [list(input().strip()) for _ in range(R)]

# 13 sec
plane = []

for _ in range(R):
    # 13 sec
    # line = list(input().strip())

    # 12 sec
    line = list(input().rstrip())
    plane.append(line)

# 12 sec
# alphabet = dict()
#
# for idx in range(65, 91):
#     alphabet.setdefault(chr(idx), 1)
#
# alphabet[plane[0][0]] -= 1

# 11 sec
alphabet = set()
alphabet.add(plane[0][0])

dfs(0, 0, 1)

print(mx)

# end = time.time()
# print(f"{end - start:.5f} sec")