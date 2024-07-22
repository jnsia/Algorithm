T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    cnt = 0

    while len(numbers) > 0:
        if numbers[0] != max(numbers):
            temp = numbers.pop(0)
            numbers.append(temp)

            if M == 0:
                M = len(numbers) - 1
            else:
                M -= 1
        else:
            max_num = numbers.pop(0)
            cnt += 1

            if M == 0:
                break

            M -= 1

    print(cnt)