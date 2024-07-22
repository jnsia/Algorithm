A, B, C = map(int, input().split())

if C - B == 0:
    x = -1
else:
    x = A / (C - B)

if x <= 0:
    print(-1)
else:
    print(int(x + 1))