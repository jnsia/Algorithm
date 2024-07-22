def binary_sum(start, end, node, left, right):
    if start > right or end < left:
        return 0

    if start <= left and end >= right:
        return segment_tree[node]

    mid = (left + right) // 2

    left_result = binary_sum(start, end, node * 2, left, mid)
    right_result = binary_sum(start, end, node * 2 + 1, mid + 1, right)

    return left_result + right_result


from math import log2

N, M, K = map(int, input().split())

# --- init ---

# 말단 노드의 층과 번호를 기록할 시작점 찾기
size = 2 ** (int(log2(N) + 1))
segment_tree = [0] * (size * 2)

# segment 트리 말단에 값 할당
for idx in range(N):
    number = int(input())
    segment_tree[size + idx] = number

# 부모 노드에 값을 더함
for idx in range(size - 1, 0, -1):
    segment_tree[idx] = segment_tree[idx * 2] + segment_tree[idx * 2 + 1]


for _ in range(M + K):
    a, b, c = map(int, input().split())

    # --- update ---
    if a == 1:
        cur_idx = size + b - 1
        diff_value = c - segment_tree[cur_idx]

        while cur_idx:
            segment_tree[cur_idx] += diff_value
            cur_idx = cur_idx // 2
    # --- sum ---
    else:
        sum_value = binary_sum(b, c, 1, 1, size)
        print(sum_value)


