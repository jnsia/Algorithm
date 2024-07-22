# 일단 0이 있어야 함
# 30 60 90 120 150 180 210 240 270 300 330 360 ... 1270 1310

N = list(input())

if N.count('0') == 0:
    print(-1)
else:
    sum_num = 0

    for i in range(len(N)):
        sum_num += int(N[i])

    if sum_num % 3 == 0:
        N.sort(reverse=True)
        print(*N, sep="")
    else:
        print(-1)