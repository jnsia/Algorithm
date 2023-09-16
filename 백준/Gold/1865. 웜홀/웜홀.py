import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    times = [25000001] * (N + 1)
    edges = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())

        edges[S].append([T, E])
        edges[E].append([T, S])

    for _ in range(W):
        S, E, T = map(int, input().split())

        edges[S].append([-T, E])

    times[1] = 0
    is_loop = False

    for repeat in range(N):
        for vertex in range(1, N + 1):
            for time, node in edges[vertex]:
                if times[node] > times[vertex] + time:
                    times[node] = times[vertex] + time

                    if repeat == N - 1:
                        is_loop = True

    if is_loop:
        print('YES')
    else:
        print('NO')