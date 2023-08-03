T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    result = [0] * 5

    while N > 1:
        if N % 2 == 0:
            result[0] += 1
            N = N // 2
        elif N % 3 == 0:
            result[1] += 1
            N = N // 3
        elif N % 5 == 0:
            result[2] += 1
            N = N // 5
        elif N % 7 == 0:
            result[3] += 1
            N = N // 7
        elif N % 11 == 0:
            result[4] += 1
            N = N // 11
    
    print(f'#{tc}', end=" ")

    for i in result:
        print(i, end=" ")
    print()