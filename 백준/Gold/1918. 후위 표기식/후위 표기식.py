S = input()
stack = []
result = ''

for w in S:
    if ord('A') <= ord(w) <= ord('Z'):
        result += w
        continue

    if w == '(':
        stack.append(w)

    if w == ')':
        while stack and stack[-1] != '(':
            tmp = stack.pop()
            result += tmp

        stack.pop()

    if w in ['+', '-']:
        while stack and stack[-1] not in ['(', ')']:
            tmp = stack.pop()
            result += tmp

        stack.append(w)

    if w in ['*', '/']:
        if stack and stack[-1] in ['*', '/']:
            tmp = stack.pop()
            result += tmp
        stack.append(w)

while stack:
    tmp = stack.pop()
    result += tmp

print(result)