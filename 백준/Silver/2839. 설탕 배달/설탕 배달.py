import sys

N = int(input())

five = [i for i in range(0, N + 1, 5)]
three = [j for j in range(0, N + 1, 3)]

arr = []

for x in five:
    for y in three:
        if x + y == N:
            arr.append((x / 5) + (y / 3))

for xx in five:
    for xxx in five:
        if xx + xxx == N:
            arr.append((xx / 5) + (xxx / 5))

for yy in three:
    for yyy in three:
        if yy + yyy == N:
            arr.append((yy / 3) + (yyy / 3))

if len(arr) == 0:
    print(-1)
else:
    print(int(sorted(arr)[0]))