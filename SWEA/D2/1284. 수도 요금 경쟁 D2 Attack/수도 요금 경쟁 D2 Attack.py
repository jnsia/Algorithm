T = int(input())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{t}', end=" ")

    a = P * W

    if W > R:
        b = Q + (W - R) * S
    else:
        b = Q

    print(min(a, b))