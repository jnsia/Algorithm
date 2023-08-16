T = 10

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    text = input()

    SUM = 0

    for word in text:
        if word != '+':
            SUM += int(word)

    print(SUM)