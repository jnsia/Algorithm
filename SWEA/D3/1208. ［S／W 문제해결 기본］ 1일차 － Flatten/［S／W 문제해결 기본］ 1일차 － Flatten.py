def quick_sort(arr):
    new_arr = arr[:]

    if not new_arr:
        return []

    pivot = new_arr[0]
    tail = new_arr[1:]

    left = list()
    right = list()

    for i in tail:
        if pivot > i:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

T = 10

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    boxes = list(map(int, input().split()))

    for i in range(N):
        boxes = quick_sort(boxes)

        if boxes[-1] - boxes[0] <= 1:
            break

        boxes[-1] -= 1
        boxes[0] += 1

    boxes = quick_sort(boxes)
    res = boxes[-1] - boxes[0]
    print(res)