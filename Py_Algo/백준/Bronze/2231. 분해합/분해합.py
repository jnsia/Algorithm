def help(n):
    result = n
    numbers = list(str(n))

    for i in numbers:
        result += int(i)

    return result

N = int(input())

for j in range(N):
    if help(j) == N:
        print(j)
        break
    elif j + 1 == N:
        print(0)