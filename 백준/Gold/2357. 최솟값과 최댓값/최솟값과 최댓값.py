def find(start, end, node, left, right):
    global min_value
    global max_value

    if start > right or end < left:
        return

    if start <= left and end >= right:
        min_value = min(min_value, min_tree[node])
        max_value = max(max_value, max_tree[node])
        return

    mid = (left + right) // 2
    find(start, end, node * 2, left, mid)
    find(start, end, node * 2 + 1, mid + 1, right)


from math import log2

MAX = 1000000001

N, M = map(int, input().split())
size = 2 ** int(log2(N - 1) + 1)
min_tree = [MAX] * (size * 2)
max_tree = [0] * (size * 2)

# init
for idx in range(N):
    number = int(input())
    min_tree[size + idx] = number
    max_tree[size + idx] = number

    cur_idx = size + idx

    while cur_idx:
        cur_idx //= 2
        min_tree[cur_idx] = min(min_tree[cur_idx * 2], min_tree[cur_idx * 2 + 1])
        max_tree[cur_idx] = max(max_tree[cur_idx * 2], max_tree[cur_idx * 2 + 1])

# find
for _ in range(M):
    a, b = map(int, input().split())

    min_value = MAX
    max_value = 0
    find(a, b, 1, 1, size)
    print(min_value, max_value)

