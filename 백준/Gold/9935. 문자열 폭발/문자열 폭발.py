String = input()
bomb = input()
idx = 0
stack = []

for word in String:
    stack.append(word)

    explosion = 1

    while len(stack) >= len(bomb):
        if stack[-explosion] == bomb[-explosion]:
            explosion += 1

            if explosion == len(bomb) + 1:
                for _ in range(explosion - 1):
                    stack.pop()
                explosion = 1
        else:
            explosion = 1
            break

explosion = 1

while len(stack) >= len(bomb):
    if stack[-explosion] == bomb[-explosion]:
        explosion += 1

        if explosion == len(bomb) + 1:
            for _ in range(explosion - 1):
                stack.pop()
            explosion = 1
    else:
        explosion = 1
        break

if stack:
    print(*stack, sep='')
else:
    print('FRULA')