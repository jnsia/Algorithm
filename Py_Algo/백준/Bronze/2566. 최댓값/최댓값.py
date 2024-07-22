numbers_map = [[x for x in list(map(int, input().split()))] for _ in range(9)]

max_num = 0
i_index = 0
j_index = 0

for i in range(9):
    for j in range(9):
        if numbers_map[i][j] >= max_num:
            max_num = numbers_map[i][j]
            i_index = i + 1
            j_index = j + 1

print(max_num)
print(i_index, j_index)
