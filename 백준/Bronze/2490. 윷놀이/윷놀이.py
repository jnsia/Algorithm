for _ in range(3):
    a, b, c, d = map(int, input().split())
    res = a + b + c + d
    if res == 0:
        print('D')
    elif res == 1:
        print('C')
    elif res == 2:
        print('B')
    elif res == 3:
        print('A')
    else:
        print('E')