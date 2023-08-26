def check_magnetic(num, drct):
    visited[num] = True
    
    if 0 <= num - 1 and magnet_list[num - 1][2] != magnet_list[num][6] and visited[num - 1] == False:
        check_magnetic(num - 1, -drct)
        
        if drct == -1:
            magnet_list[num - 1] = clock_direction(magnet_list[num - 1])
        else:
            magnet_list[num - 1] = unclock_direction(magnet_list[num - 1])
            

    if num + 1 <= 3 and magnet_list[num + 1][6] != magnet_list[num][2] and visited[num + 1] == False:
        check_magnetic(num + 1, -drct)

        if drct == -1:
            magnet_list[num + 1] = clock_direction(magnet_list[num + 1])
        else:
            magnet_list[num + 1] = unclock_direction(magnet_list[num + 1])


def clock_direction(arr):
    tmp = arr.pop()
    arr.insert(0, tmp)
    return arr


def unclock_direction(arr):
    tmp = arr.pop(0)
    arr.append(tmp)
    return arr


# 위: idx = 0 / 왼쪽: idx = 6 / 오른쪽: idx = 2
magnet1 = list(map(int, list(input())))
magnet2 = list(map(int, list(input())))
magnet3 = list(map(int, list(input())))
magnet4 = list(map(int, list(input())))

magnet_list = [magnet1, magnet2, magnet3, magnet4]

K = int(input())

for _ in range(K):
    visited = [False] * 4
    magnet_num, direction = map(int, input().split())
    magnet_num -= 1
    check_magnetic(magnet_num, direction)
    
    if direction == 1:
        magnet_list[magnet_num] = clock_direction(magnet_list[magnet_num])
    else:
        magnet_list[magnet_num] = unclock_direction(magnet_list[magnet_num])

score = 0

for idx in range(4):
    score += magnet_list[idx][0] * (2 ** idx)

print(score)