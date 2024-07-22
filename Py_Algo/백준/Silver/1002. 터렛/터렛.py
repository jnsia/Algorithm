N = int(input())

for tc in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    distance = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5

    if distance == 0:
        if r1 == r2:
            if r1 == r2 == 0:
                print(1)
            else:
                print(-1)
        else:
            print(0)
    else:
        if r1 + r2 == distance or abs(r2 - r1) == distance:
            print(1)
        elif r1 + r2 < distance or distance + r1 < r2 or distance + r2 < r1:
            print(0)
        else:
            print(2)

