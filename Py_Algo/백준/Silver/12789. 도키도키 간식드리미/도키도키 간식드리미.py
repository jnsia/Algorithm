import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
number = 1

while arr or stack:
    temp = arr.pop(0)

    if temp != number:
        stack.append(temp)
    elif temp == number:
        number += 1

    while stack:
        if stack[-1] == number:
            stack.pop()
            number += 1
        else:
            break
    if stack:
        if len(arr) == 0 and stack[-1] != number:
            print('Sad')
            break

# print(stack)

if number == N + 1:
    print('Nice')