T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')

    N = N // 10

    credits = [0,0,0,0,0,0,0,0]

    while N > 0:
        if N >= 5000:
            N -= 5000
            credits[0] += 1
        elif N >= 1000:
            N -= 1000
            credits[1] += 1
        elif N >= 500:
            N -= 500
            credits[2] += 1
        elif N >= 100:
            N -= 100
            credits[3] += 1
        elif N >= 50:
            N -= 50
            credits[4] += 1
        elif N >= 10:
            N -= 10
            credits[5] += 1
        elif N >= 5:
            N -= 5
            credits[6] += 1
        elif N >= 1:
            N -= 1
            credits[7] += 1

    for j in credits:
        print(j, end=" ")
    print()