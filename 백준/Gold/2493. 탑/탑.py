N = int(input())
buildings = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(N):
    building = buildings[i]

    while stack:
        if buildings[stack[-1]] > building:
            break
        stack.pop()

    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)