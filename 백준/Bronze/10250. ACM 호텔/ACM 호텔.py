T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    hotel = [[0 for _ in range(W)] for _ in range(H)]

    count = 0
    break_btn = False

    for y in range(W):
        for x in range(H):
            hotel[H - 1 - x][y] = 100 * (x+1) + (y+1)
            count += 1

            if count == N:
                print(hotel[H - 1 - x][y])
                break_btn = True
                break

        if break_btn:
            break