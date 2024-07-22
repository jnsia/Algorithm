# N, M = map(int, input().split())
# N = int(input())

max = 0
index = 0

for x in range(9):
    n = int(input())

    if n >= max:
        max = n
        index = x

print(max)
print(index + 1)