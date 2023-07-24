import sys

while True:
    s = list(input())

    if s[0] == '.':
        break

    stack = []
    result = 'yes'

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                temp = stack.pop()
            else:
                result = 'no'
                break

            if temp != '(':
                result = 'no'
                break
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack:
                temp = stack.pop()
            else:
                result = 'no'
                break

            if temp != '[':
                result = 'no'
                break

    if stack:
        result = 'no'
    
    print(result)