T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}', end=" ")

    i = 1
    a = 0
    arr = set()

    while True:
        li = list(str(N * i))

        for x in li:
            arr.add(x)

        if len(arr) == 10:
            a = N * i
            break

        i += 1

    print(a)