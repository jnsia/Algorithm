def pick_bucket(bucket, target, visit):
    global mx_honey

    new_visit = visit[:]

    if sum(target) > C:
        return

    tmp_total = 0

    for lc in target:
        tmp_total += lc * lc

    if tmp_total > mx_honey:
        mx_honey = tmp_total

    for bc in range(M):
        if new_visit[bc] == False:
            new_visit[bc] = True
            pick_bucket(bucket, target + [bucket[bc]], new_visit)


def get_honey(arr):
    honey_bucket = []

    for ax, ay in arr:
        honey_bucket.append(honey[ax][ay])

    return honey_bucket


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

    res_list = []

    for worker1 in range(len(coord)):
        for worker2 in range(worker1, len(coord)):
            if not worker1 == worker2 and not is_dup(coord[worker1], coord[worker2]):
                honey1 = []
                honey2 = []

                for ax, ay in coord[worker1]:
                    honey1.append(honey[ax][ay])

                for bx, by in coord[worker2]:
                    honey2.append(honey[bx][by])

                res_list.append([honey1, honey2])

    answer = 0

    for res in res_list:
        total_honey = 0
        for work in range(2):
            mx_honey = 0

            visited = [False for _ in range(M)]
            pick_bucket(res[work], [], visited)

            total_honey += mx_honey

        if total_honey > answer:
            answer = total_honey

    print(answer)

