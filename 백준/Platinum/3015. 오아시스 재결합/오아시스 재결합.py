N = int(input())
arr = [int(input()) for _ in range(N)]

stack = []
answer = 0

for idx in range(N):
    height = arr[idx]

    while stack and stack[-1][0] < height:
        answer += stack.pop()[1]

    if not stack:
        stack.append((height, 1))
        continue

    if stack[-1][0] == height:
        cnt = stack.pop()[1]
        answer += cnt

        if stack:
            answer += 1

        stack.append((height, cnt + 1))
    else:
        stack.append((height, 1))
        answer += 1

print(answer)