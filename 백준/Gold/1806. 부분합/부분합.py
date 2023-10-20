N, S = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 1
cur = arr[0]
min_len = 100001

if arr[0] >= S:
    min_len = 1

while i < N - 1:
    if j > N - 1:
        cur -= arr[i]
        i += 1
    elif cur <= S:
        cur += arr[j]
        j += 1
    elif cur > S:
        cur -= arr[i]
        i += 1

    if cur >= S and min_len > j - i:
        min_len = j - i

if min_len == 100001:
    print(0)
else:
    print(min_len)