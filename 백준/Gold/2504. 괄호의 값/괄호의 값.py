bracket = input()
stack = []
is_correct = True

for i in bracket:
    if i in ['(', '[']:
        stack.append(i)
        continue

    if len(stack) == 0:
        if i in ['(', '[']:
            stack.append(i)
            continue
        else:
            is_correct = False
            break

    if i == ')':
        if stack[-1] in ['[', ']', ')']:
            is_correct = False
            break
        elif stack[-1] == '(':
            stack.pop()
            stack.append(2)
        else:
            tmp = 0

            while True:
                if len(stack) == 0:
                    is_correct = False
                    break

                next = stack[-1]

                if next in ['[', ']', ')']:
                    is_correct = False
                    break
                elif next == '(':
                    stack.pop()
                    stack.append(tmp * 2)
                    break
                else:
                    stack.pop()
                    tmp += next

    if i == ']':
        if stack[-1] in ['(', ')', ']']:
            is_correct = False
            break
        elif stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            tmp = 0

            while True:
                if len(stack) == 0:
                    is_correct = False
                    break

                next = stack[-1]

                if next in ['(', ')', ']']:
                    is_correct = False
                    break
                elif next == '[':
                    stack.pop()
                    stack.append(tmp * 3)
                    break
                else:
                    stack.pop()
                    tmp += next

res = 0

while stack:
    tmp = stack.pop()

    if tmp in ['(', ')', '[', ']']:
        is_correct = False
        break
    else:
        res += tmp

if is_correct:
    print(res)
else:
    print(0)
