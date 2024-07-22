T = int(input())
 
for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
 
    result = [0] * 5
    arr = [2, 3, 5, 7, 11]

    for i in range(5):
        while N % arr[i] == 0:
            result[i] += 1
            N //= arr[i]
 
    print(*result)