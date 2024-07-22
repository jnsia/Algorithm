T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    margin = 0

    for i in range(N - 2, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            margin += max_price - price[i]

    print(margin)