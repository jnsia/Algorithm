N = int(input())
total_area = 0
sx, sy = map(int, input().split())

x1_to_y2 = 0
y1_to_x2 = 0

px, py = sx, sy

for _ in range(N - 1):
    x, y = map(int, input().split())

    x1_to_y2 += px * y
    y1_to_x2 += py * x

    px, py = x, y

x1_to_y2 += px * sy
y1_to_x2 += py * sx

answer = round(abs(x1_to_y2 - y1_to_x2) / 2, 1)
print(answer)