N, M = map(int, input().split())
numbers = list(map(int, input().split()))

for x in range(N):
    if M > numbers[x]:
        print(numbers[x], end=" ")