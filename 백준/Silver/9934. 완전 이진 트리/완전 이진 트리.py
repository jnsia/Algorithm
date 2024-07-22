def order(idx, k):
    if k >= 0:
        res[K - k - 1].append(arr[idx])
        order(idx - 2 ** (k - 1), k - 1)
        order(idx + 2 ** (k - 1), k - 1)

K = int(input())
arr = [0] + list(map(int, input().split()))
res = [[] for _ in range(K)]
order((2 ** K) // 2, K - 1)
for line in res:
    print(*line)