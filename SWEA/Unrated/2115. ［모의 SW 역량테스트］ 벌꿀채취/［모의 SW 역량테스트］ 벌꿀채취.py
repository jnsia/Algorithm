def pick_bucket1(bucket, target1, visit):
    global mx_honey1

    new_visit1 = visit[:]

    if sum(target1) > C:
        return

    tmp_total = 0

    for lc in target1:
        tmp_total += lc * lc

    if tmp_total > mx_honey1:
        mx_honey1 = tmp_total

    for bc in range(M):
        if new_visit1[bc] == False:
            new_visit1[bc] = True
            pick_bucket1(bucket, target1 + [bucket[bc]], new_visit1)


def pick_bucket2(bucket, target2, visit):
    global mx_honey2

    new_visit2 = visit[:]

    if sum(target2) > C:
        return

    tmp_total = 0

    for lc in target2:
        tmp_total += lc * lc

    if tmp_total > mx_honey2:
        mx_honey2 = tmp_total

    for bc in range(M):
        if new_visit2[bc] == False:
            new_visit2[bc] = True
            pick_bucket2(bucket, target2 + [bucket[bc]], new_visit2)


def is_dup(arr1, arr2):
    result = False

    for el in arr1:
        if el in arr2:
            result = True
            break

    return result


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, M, C = map(int, input().split())

    honey = [list(map(int, input().split())) for _ in range(N)]
    coord = []

    for height in range(N):
        for width in range(N - M + 1):
            case = []

            for z in range(M):
                case.append((height, width + z))

            coord.append(case)

    answer = 0

    for worker1 in range(len(coord)):
        
        for worker2 in range(worker1, len(coord)):
            if not worker1 == worker2 and not is_dup(coord[worker1], coord[worker2]):
                total_honey = 0
                
                honey1 = []
                honey2 = []

                for ax, ay in coord[worker1]:
                    honey1.append(honey[ax][ay])

                for bx, by in coord[worker2]:
                    honey2.append(honey[bx][by])

                mx_honey1 = 0
                mx_honey2 = 0
                visited1 = [False for _ in range(M)]
                visited2 = [False for _ in range(M)]
                pick_bucket1(honey1, [], visited1)
                pick_bucket2(honey2, [], visited2)

                total_honey = mx_honey1 + mx_honey2

                if total_honey > answer:
                    answer = total_honey

    print(answer)

