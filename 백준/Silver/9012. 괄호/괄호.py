def makit(n):
    left = 0
    right = 0

    result = True

    if n[-1] == '(':
        result = False

    for i in n:
        if i == '(':
            left += 1
        elif i == ')':
            right += 1

            if left < right:
                result = False
            
    if left != right:
            result = False

    return result

T = int(input())

for i in range(T):
    n = input()

    if makit(n):
        print('YES')
    else:
        print('NO')