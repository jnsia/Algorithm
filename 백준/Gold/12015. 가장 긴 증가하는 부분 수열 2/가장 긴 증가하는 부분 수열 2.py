def binary_search(key):
    low = 0
    high = len(answer) - 1
    result = len(answer)

    while low <= high:
        mid = (low + high) // 2

        if answer[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            result = mid

    return result


N = int(input())
arr = list(map(int, input().split()))

answer = [arr[0]]

for idx in range(1, N):
    num = arr[idx]

    if num > answer[-1]:
        answer.append(num)
    else:
        result = binary_search(num)
        answer[result] = num

# print(answer)
print(len(answer))