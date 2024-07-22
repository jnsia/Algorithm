T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    S = input()

    if S == S[::-1]:
        print(1)
    else:
        print(0)