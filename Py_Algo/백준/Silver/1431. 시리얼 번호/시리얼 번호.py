def compare(a, b):
    if len(a) < len(b):
        return 1
    elif len(a) == len(b):
        a_sum = 0
        b_sum = 0

        for i in range(len(a)):
            if '0' <= a[i] <= '9':
                a_sum += int(a[i])

            if '0' <= b[i] <= '9':
                b_sum += int(b[i])

        if a_sum < b_sum:
            return 1
        elif a_sum == b_sum:
            if a < b:
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1


def sort():
    for i in range(N - 1):
        for j in range(i, N):
            if compare(arr[i], arr[j]) == -1:
                arr[i], arr[j] = arr[j], arr[i]


N = int(input())

arr = []

for n in range(N):
    arr.append(input())

sort()

print(*arr, sep="\n")