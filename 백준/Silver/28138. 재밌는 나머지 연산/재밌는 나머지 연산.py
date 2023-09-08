N, R = map(int, input().split())
target = N - R
is_check = False
res = []
ans = 0

for i in range(1, int(target ** 0.5) + 1):
    if (target % i == 0):
        res.append(i)

        if (i ** 2 != target):
            res.append(target // i)

for num in res:
    if (num > R):
        ans += num

print(ans)