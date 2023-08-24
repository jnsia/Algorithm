T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    result = True
    cnt = 0
    bread = -K

    while numbers:
        if not result:
            break

        if cnt % M == 0:
            bread += K

        while len(numbers) > 0 and numbers[0] == cnt:
            numbers.pop(0)

            if bread > 0:
                bread -= 1
            else:
                result = False
                break

        cnt += 1

    if result:
        print('Possible')
    else:
        print('Impossible')