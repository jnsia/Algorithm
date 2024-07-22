T = 10

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    in_fix = list(input())

    in_stack = []
    post_fix = []

    for word in in_fix:
        if word.isdigit():
            post_fix.append(int(word))

        if word == '+':
            while len(in_stack) > 0 and in_stack[-1] in ['+', '*']:
                tmp = in_stack.pop()
                post_fix.append(tmp)

            in_stack.append(word)

        if word == '*':
            if len(in_stack) > 0 and in_stack[-1] == '*':
                tmp = in_stack.pop()
                post_fix.append(tmp)

            in_stack.append(word)

    while len(in_stack) > 0:
        tmp = in_stack.pop()
        post_fix.append(tmp)

    post_stack = []

    for word in post_fix:
        if word not in ['+', '*']:
            post_stack.append(word)

        if word == '+':
            tmp = post_stack.pop()
            post_stack[-1] = post_stack[-1] + tmp

        if word == '*':
            tmp = post_stack.pop()
            post_stack[-1] = post_stack[-1] * tmp

    print(post_stack[0])
