N, M = map(int, input().split())
numbers = list(map(int, input().split()))

arr = []

for x in range(N):
    temp = 0
    for y in range(x + 1, N):
        for z in range(y + 1, N):
            if x != y or y != z or x != z:
                temp = numbers[x] + numbers[y] + numbers[z]
                if temp <= M:
                    arr.append(temp)

print(max(arr))