N = int(input())

total_map = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    n, m = map(int, input().split())

    for x in range(n, n + 10):
        for y in range(m, m + 10):
            total_map[x][y] = 1

count = 0

for j in range(100):
    for k in range(100):
        if total_map[j][k] == 1:
            count += 1

print(count)