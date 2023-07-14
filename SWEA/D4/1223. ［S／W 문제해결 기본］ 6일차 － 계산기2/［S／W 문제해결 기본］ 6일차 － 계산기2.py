# T = int(input())

for t in range(1, 11):
    N = int(input())
    st = input()
    print(f'#{t}', end=" ")

    stack = []
    post = ''

    for i in st:
        if i == '+' or i == '*':
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == '+' and i == '*':
                stack.append(i)
            elif stack[-1] == i:
                post += i
            elif stack[-1] == '*' and i == '+':
                post += '*'
                del stack[-1]
                stack.append(i)
        else:
            post += i

    for i in range(len(stack)):
        post += stack[-1]
        del stack[-1]

    # print(post)

    for x in post:
        if x == '*':
            temp = int(stack[-1]) * int(stack[-2])
            del stack[-1]
            del stack[-1]
            stack.append(temp)
        elif x == '+':
            temp = int(stack[-1]) + int(stack[-2])
            del stack[-1]
            del stack[-1]
            stack.append(temp)
        else:
            stack.append(int(x))

    print(stack[0])