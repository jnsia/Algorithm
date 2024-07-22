def func(lst, m):
    result = []

    if m == 1:
        for i in lst:
            result.append([i])
    else:
        for i in range(len(lst)):
            ans = [i for i in lst]
            ans.remove(lst[i])

            for j in func(ans, m - 1):
                result.append([lst[i]] + j)

    return result

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [x for x in range(1, N + 1)]

for x in func(lst, M):
    print(*x)