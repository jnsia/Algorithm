A, B = map(int, input().split())
arr = [0]

for i in range(1, 1001):
    for j in range(i):
        arr.append(i)

answer = 0

for i in range(A, B + 1):
    answer += arr[i]

print(answer)