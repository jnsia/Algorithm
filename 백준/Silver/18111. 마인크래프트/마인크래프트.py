import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = []

for _ in range(N):
    ground.append(list(map(int, input().split())))

result = [256 * 500 * 500, 0]

for key in range(257):
    temp_time = 0
    inven = B

    for x in ground:
        for y in x:
            if key > y:
                temp_time += key - y
                inven -= key - y
            else:
                temp_time += (y - key) * 2
                inven += y - key

    if inven >= 0:
        if result[0] >= temp_time:
            result[0] = temp_time
            result[1] = key

print(*result)
