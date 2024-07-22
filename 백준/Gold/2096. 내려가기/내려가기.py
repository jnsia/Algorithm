N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for row in range(N):
    copy_max = dp_max[:]
    copy_min = dp_min[:]

    for col in range(3):
        if col == 0:
            dp_max[col] = matrix[row][col] + max(copy_max[col], copy_max[col + 1])
            dp_min[col] = matrix[row][col] + min(copy_min[col], copy_min[col + 1])
        elif col == 1:
            dp_max[col] = matrix[row][col] + max(copy_max[col], copy_max[col - 1], copy_max[col + 1])
            dp_min[col] = matrix[row][col] + min(copy_min[col], copy_min[col - 1], copy_min[col + 1])
        elif col == 2:
            dp_max[col] = matrix[row][col] + max(copy_max[col], copy_max[col - 1])
            dp_min[col] = matrix[row][col] + min(copy_min[col], copy_min[col - 1])

print(max(dp_max), min(dp_min))
