def div(paper, num, x, y):
    global white
    global blue

    res = ''

    if num == 0:
        return False

    tmp = num // 2

    zro = 0
    one = 0

    for n in range(x, x + num):
        for m in range(y, y + num):
            if paper[n][m]:
                zro += 1
            else:
                one += 1

    if zro == num * num:
        return '1'
    elif one == num * num:
        return '0'
    else:
        for i in range(x, x + num, tmp):
            for j in range(y, y + num, tmp):
                res += div(paper, tmp, i, j)

    return '(' + res + ')'


N = int(input())
paper = [list(map(int, list(input()))) for _ in range(N)]

print(div(paper, N, 0, 0))