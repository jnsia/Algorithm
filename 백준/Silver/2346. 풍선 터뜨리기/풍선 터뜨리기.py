def move_arr(arr, n):
    new_arr = arr[:]

    if len(new_arr) == 0:
        return new_arr

    if n > 0:
        for _ in range(n - 1):
            temp = new_arr.pop(0)
            new_arr.append(temp)
    else:
        n = -n

        for _ in range(n):
            temp = new_arr.pop()
            new_arr.insert(0, temp)

    return new_arr

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

numbers = [i for i in range(1, N + 1)]

seq = []

for _ in range(N):
    temp = numbers.pop(0)
    seq.append(temp)

    numbers = move_arr(numbers, arr[temp - 1])
print(*seq)