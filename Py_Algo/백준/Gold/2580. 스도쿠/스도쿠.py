def check(plane, x, y):
    numbers = set()
    result = []

    for i in range(9):
        numbers.add(plane[i][y])
        numbers.add(plane[x][i])

    for i in range(3):
        for j in range(3):
            numbers.add(plane[x // 3 * 3 + i][y // 3 * 3 + j])

    for i in range(1, 10):
        if i not in numbers:
            result.append(i)

    return result

def dfs(plane):
    if answer:
        return

    new_plane = []

    for line in plane:
        new_plane.append(line[:])

    for i in range(9):
        for j in range(9):
            if new_plane[i][j] == 0:
                numbers = check(new_plane, i, j)

                for num in numbers:
                    new_plane[i][j] = num
                    dfs(new_plane)

                return

    answer.append(plane)

sudoku = [list(map(int, input().split())) for _ in range(9)]
answer = []
dfs(sudoku)

for line in answer[0]:
    print(*line)
