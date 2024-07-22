T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=" ")

    N = int(input())
    numbers = list(map(int, input().split()))

    avg = sum(numbers) / len(numbers)

    cnt = 0

    for i in numbers:
        if avg >= i:
            cnt += 1

    print(cnt)