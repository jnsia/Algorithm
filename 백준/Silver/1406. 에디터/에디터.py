S = list(input())
M = int(input())
tmp_stack = []
# 초기에 커서는 맨 뒤에 있음
for m in range(M):
    command = list(map(str, input().split()))

    if command[0] == 'P':
        S.append(command[1])

    if command[0] == 'L' and len(S) > 0:
        tmp = S.pop()
        tmp_stack.append(tmp)

    if command[0] == 'D' and len(tmp_stack) > 0:
        tmp = tmp_stack.pop()
        S.append(tmp)

    if command[0] == 'B' and len(S) > 0:
        S.pop()

while tmp_stack:
    tmp = tmp_stack.pop()
    S.append(tmp)

print(*S, sep='')