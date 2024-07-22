T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    numbers = list(map(int, input().split()))
    total = []

    for n1 in range(N):
        for n2 in range(n1, N):
            if n1 != n2:
                total.append(numbers[n1] * numbers[n2])

    danzo = []

    for num in total:
        is_danzo = True
        target = num

        while target > 0:
            back = target % 10
            target = target // 10
            front = target % 10

            if front > back:
                is_danzo = False
                break

        if is_danzo:
            danzo.append(num)

    if danzo:
        print(max(danzo))
    else:
        print(-1)