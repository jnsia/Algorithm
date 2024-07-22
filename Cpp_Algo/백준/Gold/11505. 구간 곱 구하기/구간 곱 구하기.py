def times_out(left, right, start, end, now):
    if left > end or right < start:
        return 1

    if left >= start and end >= right:
        return tree[now]

    mid = (left + right) // 2
    return times_out(left, mid, start, end, now * 2) * times_out(mid + 1, right, start, end, now * 2 + 1) % MOD


def define_height(num):
    result = 1

    while num > 2 ** result:
        result += 1

    return result


import sys
input = sys.stdin.readline

MOD = 1000000007

N, M, K = map(int, input().split())
height = define_height(N)
size = 2 ** height
tree = [1] * (2 ** (height + 1))

for i in range(N):
    num = int(input())
    tree[size + i] = num

for i in range(size - 1, 0, -1):
    tree[i] = tree[i * 2] * tree[i * 2 + 1] % MOD

for i in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        now = size + b - 1
        tree[now] = c
        now //= 2

        while now > 0:
            tree[now] = tree[now * 2] * tree[now * 2 + 1] % MOD
            now //= 2

    if a == 2:
        result = times_out(1, size, b, c, 1) % MOD
        print(result)
