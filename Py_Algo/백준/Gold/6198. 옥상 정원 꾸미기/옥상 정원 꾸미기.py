N = int(input())
buildings = [int(input()) for _ in range(N)]
result = [0] * N
stack = []

for i in range(N):
    building = buildings[i]

    while stack:
        if stack[-1] > building:
            break
        stack.pop()

    result[i] = len(stack)
    stack.append(building)

print(sum(result))