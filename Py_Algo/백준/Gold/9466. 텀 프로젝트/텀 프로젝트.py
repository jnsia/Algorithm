def dfs(choice):
    global cnt

    visited[choice] = True
    collected.append(choice)
    student = students[choice]

    if visited[student]:
        if student in collected:
            cnt += len(collected[collected.index(student):])
        return
    else:
        dfs(students[choice])


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

T = int(input())

for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    cnt = 0

    for num in range(1, N + 1):
        if not visited[num]:
            collected = []
            dfs(num)

    print(N - cnt)