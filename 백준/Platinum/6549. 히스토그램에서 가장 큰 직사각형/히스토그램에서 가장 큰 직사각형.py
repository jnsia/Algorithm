while True:
    N, *arr = map(int, input().split())

    if N == 0:
        break

    min_height = min(arr)
    dists = [0] * N
    stack = []
    height = 0

    for idx in range(N):
        if not stack:
            stack.append((idx, arr[idx]))
            height = arr[idx]
            continue

        while stack and arr[idx] < stack[-1][1]:
            temp = stack.pop()
            dists[temp[0]] = idx - temp[0]

        stack.append((idx, arr[idx]))
        # print(stack)

    while stack:
        temp = stack.pop()
        dists[temp[0]] = N - temp[0]

    for idx in range(N - 1, -1, -1):
        if not stack:
            stack.append((idx, arr[idx]))
            height = arr[idx]
            continue

        while stack and arr[idx] < stack[-1][1]:
            temp = stack.pop()
            dists[temp[0]] += temp[0] - idx

        stack.append((idx, arr[idx]))
        # print(stack)

    while stack:
        temp = stack.pop()
        dists[temp[0]] += temp[0] + 1

    answer = 0

    for idx in range(N):
        answer = max((dists[idx] - 1) * arr[idx], answer)

    # print(dists)
    print(answer)