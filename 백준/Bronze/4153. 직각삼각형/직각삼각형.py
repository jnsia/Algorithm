while True:
    l = list(map(int, input().split()))
    
    if l.count(0) == 3:
        break
    
    l.sort()

    if (l[0] ** 2) + (l[1] ** 2) == l[2] ** 2:
        print('right')
    else:
        print('wrong')