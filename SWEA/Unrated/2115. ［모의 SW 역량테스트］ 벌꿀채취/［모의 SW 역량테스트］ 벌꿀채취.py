def pick_bucket(bucket, target):
    global mx_honey

    if sum(target) > C:
        return

    tmp_total = 0

    for lc in target:
        tmp_total += lc * lc

    if tmp_total > mx_honey:
        mx_honey = tmp_total

    for bc in range(M):
        if visited[bc] == False:
            visited[bc] = True
            pick_bucket(bucket, target + [bucket[bc]])
            visited[bc] = False


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


def search_coord():
    for height in range(N):
        for width in range(N - M + 1):
            case = []

            for z in range(M):
                case.append((height, width + z))

            coord.append(case)


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    coord = []
    search_coord()

    res_list = []

    for worker1 in coord:
        for worker2 in coord:
            if not worker1 == worker2 and not is_dup(worker1, worker2):
                res_list.append([get_honey(worker1), get_honey(worker2)])

    answer = 0

    for res in res_list:
        total_honey = 0
        for work in range(2):
            mx_honey = 0
            visited = [False for _ in range(M)]
            pick_bucket(res[work], [])
            total_honey += mx_honey

        if total_honey > answer:
            answer = total_honey

    print(answer)