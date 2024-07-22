N, M = map(int, input().split())

arr = []

for _ in range(N):
    s, e = map(int, input().split())

    if s > e:
        arr.append((e, s))

arr.sort(key=lambda x: -x[1])

ans = M

s, e = arr[0]

for i in range(1, len(arr)):
    ns, ne = arr[i]

    if s <= ne:
        s = min(ns, s)
    else:
        ans += (e - s) * 2
        s, e = ns, ne

ans += (e - s) * 2

print(ans)