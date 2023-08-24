T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    arr = [list(input()) for _ in range(5)]
    res = ''

    for i in range(15):
        for j in range(5):
            try:
                res += arr[j][i]
            except:
                pass

    print(res)