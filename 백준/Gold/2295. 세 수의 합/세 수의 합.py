def bs(key, end):
    low = 0
    high = end - 1

    while low <= high:
        mid = (low + high) // 2

        if right[mid][2] == key:
            return U[right[mid][1]]
        elif right[mid][2] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1


N = int(input())
U = list()

for i in range(N):
    temp = int(input())
    U.append(temp)

U.sort()

left = list()
right = list()

for i in range(N):
    for j in range(N):
        left.append((i, j, U[i] + U[j]))

for i in range(N):
    for j in range(N):
        temp = U[j] - U[i]

        if temp >= 0:
            right.append((i, j, temp))

right.sort(key=lambda x: x[2])
answer = 0

for i in range(len(left)):
    result = bs(left[i][2], len(right))

    if result > 0:
        answer = max(answer, result)

print(answer)