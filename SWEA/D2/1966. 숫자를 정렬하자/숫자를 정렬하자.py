def bubble(arr, n):
    lst = arr[:]

    for i in range(n - 1):
        for j in range(n - 1):
            if lst[j + 1] < lst[j]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = bubble(arr, N)

    print(f'#{test_case}', *sorted_arr)