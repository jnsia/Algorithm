size = int(input())
elements = list(map(int, input().split()))
counting = [0] * 1000001

for elem in elements:
    counting[elem] += 1

stack = []
answer = [-1] * size

for idx in range(size):
    elem = elements[idx]

    if not stack:
        stack.append(idx)
        continue

    prev_elem = elements[stack[-1]]

    while stack and counting[prev_elem] < counting[elem]:
        temp = stack.pop()
        answer[temp] = elem

        if stack:
            prev_elem = elements[stack[-1]]

    stack.append(idx)

print(*answer)