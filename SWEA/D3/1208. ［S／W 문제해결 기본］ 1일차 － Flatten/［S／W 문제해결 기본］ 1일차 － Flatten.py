def bubble(arr):
    arr_len = 0

    for _ in arr:
        arr_len += 1

    for x in range(arr_len):
        for y in range(arr_len - 1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]

    return arr

T = 10

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        lst = bubble(lst)
        lst[-1] -= 1
        lst[0] += 1
    
    lst = bubble(lst)

    print(f'#{tc}', lst[-1] - lst[0])