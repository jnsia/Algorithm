T = 10

for test_case in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    result = 0

    for i in range(2, N - 2):
        arr = [li[i-2], li[i-1], li[i+1], li[i+2]]
        arr.sort()

        if li[i] <= arr[-1]:
            continue
        else:
            result += li[i] - arr[-1]
    
    print(f'#{test_case}', result)