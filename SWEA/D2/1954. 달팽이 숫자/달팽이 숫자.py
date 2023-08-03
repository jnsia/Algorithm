T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())

    visited = set()
    visited.add((0, 0))
    route = [(0, 0)]

    x = 0
    y = 0

    while True:
        while True:
            if 0 <= y + 1 < N and (x, y + 1) not in visited:
                y += 1
                route.append((x,y))
                visited.add((x,y))
            else:
                break

        while True:
            if 0 <= x + 1 < N and (x + 1, y) not in visited:
                x += 1
                route.append((x,y))
                visited.add((x,y))
            else:
                break

        while True:
            if 0 <= y - 1 < N and (x, y - 1) not in visited:
                y -= 1
                route.append((x,y))
                visited.add((x,y))
            else:
                break

        while True:
            if 0 <= x - 1 < N and (x - 1, y) not in visited:
                x -= 1
                route.append((x,y))
                visited.add((x,y))
            else:
                break

        if len(route) == N * N:
            break

    NxN_map = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N * N):
        NxN_map[route[i][0]][route[i][1]] = i + 1

    for map in NxN_map:
        print(*map)