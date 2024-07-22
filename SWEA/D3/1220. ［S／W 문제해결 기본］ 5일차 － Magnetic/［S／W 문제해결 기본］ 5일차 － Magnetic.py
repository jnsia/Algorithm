def magnetic(arr):
    deadlock_num = 0

    is_n = False

    for n in range(100):
        if arr[n] == 1:
            is_n = True

        if arr[n] == 2 and is_n:
            deadlock_num += 1
            is_n = False

    return deadlock_num

T = 10

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    not_table = [list(map(int, input().split())) for _ in range(N)]
    # 왼쪽이 N극... N극 성질의 자성체는 1
    # 오른쪽이 S극... S극 성질의 자성체는 2
    table = list((map(list, zip(*not_table))))

    total_deadlock_num = 0

    for line in table:
        total_deadlock_num += magnetic(line)

    print(total_deadlock_num)