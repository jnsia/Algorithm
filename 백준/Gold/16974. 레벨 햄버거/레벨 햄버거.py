N, X = map(int, input().split())

layer = 1
level = 0

while level < N:
    layer = layer * 2 + 3
    level += 1

low = 1
high = layer

answer = 0

while True:
    mid = (low + high) // 2

    if mid == X:
        answer += 1
        answer += 2 ** level - 1
        level -= 1
        break
    elif low == X:
        break
    elif high == X:
        answer += 2 ** (level + 1) - 1
        break

    if mid < X:
        low = mid + 1
        high -= 1
        answer += 2 ** level - 1
        level -= 1
        answer += 1
    else:
        low += 1
        high = mid - 1
        level -= 1

print(answer)