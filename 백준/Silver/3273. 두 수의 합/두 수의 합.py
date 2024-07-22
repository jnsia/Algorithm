N = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()
# print(numbers)

cnt = 0
left = 0
right = N - 1

while left < right:
    if numbers[left] + numbers[right] == x:
        left = 0
        right -= 1
        cnt += 1
    elif numbers[left] + numbers[right] < x:
        left += 1
    else:
        right -= 1

    # print(left, right, numbers[left] + numbers[right])

print(cnt)