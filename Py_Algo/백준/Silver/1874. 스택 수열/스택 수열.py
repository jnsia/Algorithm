import sys
input = sys.stdin.readline

N = int(input())

stack = list()
stack_hist = list()

n = 1
res = True

for t in range(N):
    S = int(input())

    while True:
        if S < n:
            if S == stack[-1]:
                stack.pop()
                stack_hist.append('-')
                break
            else:
                res = False
                break
        else:
            stack.append(n)
            stack_hist.append('+')
            n += 1

if res:
    print(*stack_hist, sep="\n")
else:
    print('NO')