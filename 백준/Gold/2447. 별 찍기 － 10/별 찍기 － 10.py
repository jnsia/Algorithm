def star(lst, n):
    if n != 3:
        new_lst = star(lst, n // 3)
    else:
        new_lst = [['*']]

    for x in range(n):
        for y in range(n):
            if n // 3 <= x < n * 2 // 3 and n // 3 <= y < n * 2 // 3:
                lst[x][y] = ' '
            else:
                if n != 3:
                    lst[x][y] = new_lst[x % (n // 3)][y % (n // 3)]
    return lst

import sys
input = sys.stdin.readline

N = int(input())

lst = [['*' for _ in range(N)] for _ in range(N)]

for i in star(lst, N):
    print(*i, sep="")