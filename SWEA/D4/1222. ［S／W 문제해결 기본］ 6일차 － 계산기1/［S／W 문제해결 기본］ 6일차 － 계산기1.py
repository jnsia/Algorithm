# T = int(input())

for t in range(1, 11):
    N = int(input())
    st = input()
    print(f'#{t}', end=" ")

    stack = []
    post = ''

    for i in st:
        if len(stack) == 0 and i == '+':
            stack.append(i)
        elif len(stack) != 0 and i == '+':
            post += i
        else:
            post += i

    for i in stack:
        post += i
        stack.remove(i)

    # print(post)

    result = 0

    for x in post:
        if x == '+':
            pass
        else:
            stack.append(int(x))

    print(sum(stack))