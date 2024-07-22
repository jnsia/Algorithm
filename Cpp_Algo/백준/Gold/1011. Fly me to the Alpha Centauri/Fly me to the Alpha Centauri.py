T = int(input())

for tc in range(T):
    x, y = map(int, input().split())
    dist = y - x
    sqr = int(dist ** 0.5)

    if sqr ** 2 == dist:
        print(2 * sqr - 1)
    else:
        if ((sqr + 1) ** 2 + sqr ** 2 + 1) // 2 > dist:
            print(2 * sqr)
        else:
            print(2 * sqr + 1)
