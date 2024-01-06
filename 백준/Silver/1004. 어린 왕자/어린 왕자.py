T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())

    cnt = 0

    for _ in range(N):
        x, y, r = map(int, input().split())

        dis1 = (x1 - x) ** 2 + (y1 - y) ** 2
        dis2 = (x2 - x) ** 2 + (y2 - y) ** 2
        r2 = r * r

        if r2 > dis1 and r2 > dis2:
            pass
        elif r2 > dis1:
            cnt += 1
        elif r2 > dis2:
            cnt += 1

    print(cnt)
    