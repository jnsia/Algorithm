from collections import deque

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    func = input().strip()

    D_cnt = func.count('D')

    N = int(input())
    
    lst = input().strip('[]\n').split(',')

    if lst[0] == '':
        lst = []
    
    if D_cnt > N:
        print('error')
        continue

    arr = deque(map(int, lst))
    
    rev = False

    for act in func:
        if act == 'R':
            if rev:
                rev = False
            else:
                rev = True
        elif act == 'D':
            if rev:
                arr.pop()
            else:
                arr.popleft()
    
    if rev:
        res = str(list(arr)[::-1]).replace(' ', '')
        print(res)
    else:
        res = str(list(arr)).replace(' ', '')
        print(res)