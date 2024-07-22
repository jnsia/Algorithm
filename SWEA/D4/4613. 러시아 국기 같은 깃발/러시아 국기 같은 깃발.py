def check(matrix, color):
    cnt = 0

    for line in matrix:
        cnt += M - line.count(color)

    return cnt


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    mn_cnt = 980309

    for idx in range(N - 2):
        for jdx in range(idx + 1, N - 1):
            cnt = 0

            white = flag[:idx + 1]
            blue = flag[idx + 1: jdx + 1]
            red = flag[jdx + 1:N]

            cnt += check(white, 'W')
            cnt += check(blue, 'B')
            cnt += check(red, 'R')

            if mn_cnt > cnt:
                mn_cnt = cnt

    print(mn_cnt)