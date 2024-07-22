def distance_sum(arr):
    res = 0

    for i in range(4):
        cnt = 0
        
        for j in range(3):
            if arr[j][i] in ['I', 'N', 'F', 'J']:
                cnt += 1

        if cnt == 0 or cnt == 3:
            continue
        else:
            res += 2

    return res

def dfs(num, people, collect):
    global mn

    collected = collect[:]

    if num == 3:
        tmp = distance_sum(people)

        if mn > tmp:
            mn = tmp

        return
    
    for i in range(N):
        if collected[i] == False:
            collected[i] = True
            dfs(num + 1, people + [students[i]], collected)


import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    students = list(map(str, input().split()))
    collected = [False] * N

    mn = 100001

    if N > 32:
        print(0)
    else:
        dfs(0, [], collected)
        print(mn)