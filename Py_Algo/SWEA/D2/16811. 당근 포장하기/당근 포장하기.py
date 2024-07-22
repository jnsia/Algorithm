T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    carrot = sorted(list(map(int, input().split())))

    min_num = 980309

    for i in range(N - 2):
        if carrot[i] == carrot[i + 1]:
            continue

        for j in range(i + 1, N - 1):
            if carrot[j] == carrot[j + 1]:
                continue

            small = i + 1
            middle = j - i
            big = N - j - 1

            if max(small, middle, big) > N // 2:
                continue
            else:
                ans = 0
                num = max(small, middle, big) - min(small, middle, big)

                if min_num > num:
                    min_num = num

    if min_num == 980309:
        print(-1)
    else:
        print(min_num)