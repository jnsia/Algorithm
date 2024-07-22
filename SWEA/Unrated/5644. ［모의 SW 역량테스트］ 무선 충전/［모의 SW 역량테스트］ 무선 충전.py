def set_charger(cx, cy, ran, perf, num):
    if ran == 1:
        return

    for move in range(5):
        nx = cx + dx[move]
        ny = cy + dy[move]

        if 0 <= nx < 10 and 0 <= ny < 10:
            plane[nx][ny][num] = perf
            set_charger(nx, ny, ran - 1, perf, num)


dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    M, A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    plane = [[[0] * A for _ in range(10)] for _ in range(10)]


    for bc in range(A):
        x, y, c, p = map(int, input().split())
        set_charger(y - 1, x - 1, c + 1, p, bc)
    
    ax, ay = 0, 0
    bx, by = 9, 9

    A_charge = [plane[ax][ay]]
    B_charge = [plane[bx][by]]

    for sec in range(M):
        ax, ay = ax + dx[A_move[sec]], ay + dy[A_move[sec]]
        bx, by = bx + dx[B_move[sec]], by + dy[B_move[sec]]

        A_charge.append(plane[ax][ay])
        B_charge.append(plane[bx][by])

    total_charge = 0

    for idx in range(M + 1):
        same_max = 0
        diff_max = 0
        same_max_idx = -1

        for i in range(A):
            for j in range(A):
                if i == j:
                    if A_charge[idx][i] == 0 or B_charge[idx][j] == 0:
                        tmp = max(A_charge[idx][i], B_charge[idx][j])
                    else:
                        tmp = A_charge[idx][i] // 2

                    if tmp > same_max:
                        same_max = tmp

                else:
                    tmp = A_charge[idx][i] + B_charge[idx][j]

                    if tmp > diff_max:
                        diff_max = tmp

        total_charge += max(same_max, diff_max)
                
    print(total_charge)
