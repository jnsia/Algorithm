N = int(input())

count = 1
y = 0

if N == 1:
    x = 1
    y = 1

while N > count:
    N = N - count
    count += 1

    if count % 2 == 0:
        x = N
        y = count - x + 1
    else:
        y = N
        x = count - y + 1

print(f'{x}/{y}')