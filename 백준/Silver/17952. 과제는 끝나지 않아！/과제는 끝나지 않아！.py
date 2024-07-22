N = int(input())

stack = []
score = 0

for _ in range(N):
    cmd = list(map(int, input().split()))

    if cmd[0] == 0:
        if stack:
            tmp = stack.pop()

            if tmp[2] > 1:
                tmp[2] -= 1
                stack.append(tmp)
            else:
                score += tmp[1]
    else:
        cmd[2] -= 1
        if cmd[2] == 0:
            score += cmd[1]
        else:
            stack.append(cmd)

print(score)