def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def dfs(location):
    if board[location] == 'U':
        if find(location) != find(location - M):
            union(location, location - M)
            dfs(location - M)

    if board[location] == 'D':
        if find(location) != find(location + M):
            union(location, location + M)
            dfs(location + M)

    if board[location] == 'L':
        if find(location) != find(location - 1):
            union(location, location - 1)
            dfs(location - 1)

    if board[location] == 'R':
        if find(location) != find(location + 1):
            union(location, location + 1)
            dfs(location + 1)


# U D L R
# -M +M -1 +1

N, M = map(int, input().split())
board = ""

for i in range(N):
    board += input()

parent = [num for num in range(N * M)]

for i in range(N * M):
    dfs(i)

answer = set()

for i in range(N * M):
    answer.add(parent[i])

print(len(answer))
