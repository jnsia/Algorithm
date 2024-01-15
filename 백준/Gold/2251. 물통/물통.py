def dfs(x, y, z):
    if x > A:
        return

    if y > B:
        return

    if z > C:
        return

    if not memo[x][y][z]:
        memo[x][y][z] = True

        if x + y <= A:
            dfs(x + y, 0, z)
        else:
            dfs(A, y - (A - x), z)

        if x + y <= B:
            dfs(0, x + y, z)
        else:
            dfs(x - (B - y), B, z)

        if x + z <= C:
            dfs(0, y, x + z)
        else:
            dfs(x - (C - z), y, C)

        if x + z <= A:
            dfs(x + z, y, 0)
        else:
            dfs(A, y, z - (A - x))

        if y + z <= C:
            dfs(x, 0, y + z)
        else:
            dfs(x, y - (C - z), C)

        if y + z <= B:
            dfs(x, y + z, 0)
        else:
            dfs(x, B, z - (B - y))


A, B, C = map(int, input().split())

memo = [[[False for _ in range(201)] for _ in range(201)] for _ in range(201)]

dfs(0, 0, C)

answer = []

for i in range(201):
    for j in range(201):
        if memo[0][i][j]:
            answer.append(j)

print(*sorted(answer))
