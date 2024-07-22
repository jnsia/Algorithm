import sys
input = sys.stdin.readline

N = int(input())

queue = []
wait = 1
wait_num = []

for n in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        queue.append(command[1])

        if len(queue) > wait:
            wait = len(queue)
            wait_num = []
            wait_num.append(queue[-1])
        elif len(queue) == wait:
            wait_num.append(queue[-1])

    elif command[0] == 2:
        if len(queue) > wait:
            wait = len(queue)
            wait_num = []
            wait_num.append(queue[-1])
        elif len(queue) == wait:
            wait_num.append(queue[-1])

        queue.pop(0)

print(wait, min(wait_num))
