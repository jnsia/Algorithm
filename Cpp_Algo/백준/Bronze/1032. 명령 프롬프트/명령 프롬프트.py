N = int(input())
answer = input()
memo = [True] * len(answer)

for _ in range(N - 1):
    file = input()

    for idx in range(len(file)):
        if file[idx] != answer[idx]:
            memo[idx] = False

for idx in range(len(answer)):
    if memo[idx]:
        print(answer[idx], end="")
    else:
        print('?', end="")