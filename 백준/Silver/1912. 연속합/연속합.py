N = int(input())
numbers = list(map(int, input().split()))

for i in range(1, N):
    numbers[i] = max(numbers[i - 1] + numbers[i], numbers[i])

print(max(numbers))
