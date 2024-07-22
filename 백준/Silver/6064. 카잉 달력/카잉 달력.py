

T = int(input())

for tc in range(1, T + 1):
    M, N, x, y = map(int, input().split())

    time = x

    while (time - x) % M or (time - y) % N:
        time += M

        if time > M * N + 1:
            break

    if time > M * N + 1:
        print(-1)
    else:
        print(time)