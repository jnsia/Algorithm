def replace_fish(matrix, bool_arr, dict):
    new_matrix = []

    for line in matrix:
        new_matrix.append(line[:])

    for num in range(1, 17):
        if bool_arr[num] == False:
            x, y, direction = dict[num]

            for rotate in range(8):
                nx = x + dx[(direction + rotate) % 8]
                ny = y + dy[(direction + rotate) % 8]

                if 0 <= nx < 4 and 0 <= ny < 4 and not new_matrix[nx][ny] == 99:
                    if not new_matrix[nx][ny] == 0:
                        dict[new_matrix[nx][ny]][0], dict[new_matrix[nx][ny]][1] = x, y
                    
                    dict[num][0], dict[num][1] = nx, ny
                    dict[num][2] = (direction + rotate) % 8

                    new_matrix[x][y], new_matrix[nx][ny] = new_matrix[nx][ny], new_matrix[x][y]

                    break
        
    return new_matrix, dict


def eat_fish(shark_info, matrix, bool_arr, ate_num, fish_dict):
    global mx_score

    copy_dict = {}

    for key, value in fish_dict.items():
        copy_dict[key] = value[:]

    copy_matrix, copy_dict = replace_fish(matrix, bool_arr[:], copy_dict)

    x, y, z = shark_info[:]

    is_eat = False

    for times in range(1, 4):
        nx = x + dx[z] * times
        ny = y + dy[z] * times

        if 0 <= nx < 4 and 0 <= ny < 4 and not copy_matrix[nx][ny] == 0:
            is_eat = True
            target = copy_matrix[nx][ny]
            
            bool_arr[target] = True
            copy_matrix[x][y] = 0
            copy_matrix[nx][ny] = 99
            eat_fish(copy_dict[target], copy_matrix, bool_arr[:], ate_num + target, copy_dict)
            copy_matrix[x][y] = 99
            copy_matrix[nx][ny] = target
            bool_arr[target] = False

    if not is_eat:
        if ate_num > mx_score:
            mx_score = ate_num
        return


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

fishs = dict()
space = []
mx_score = 0

for i in range(4):
    line = list(map(int, input().split()))
    
    tmp = []

    for j in range(0, 8, 2):
        fish_num = line[j]
        fishs[fish_num] = [i, j // 2, line[j + 1]]
        tmp.append(fish_num)
    
    space.append(tmp)


ate_fish = [False for _ in range(17)]

target = space[0][0]
ate_fish[target] = True
space[0][0] = 99

eat_fish(fishs[target], space, ate_fish, target, fishs)

print(mx_score)