N = int(input())

start = 2

# 3 5 9 17 33

for i in range(N):
    start += 2 ** i

print(start * start)