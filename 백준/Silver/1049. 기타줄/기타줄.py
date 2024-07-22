N, M = map(int, input().split())

min_package = 1001
min_each = 1001

for _ in range(M):
    package, each = map(int, input().split())
    min_package = min(package, min_package)
    min_each = min(each, min_each)

if min_each * 6 < min_package:
    print(N * min_each)
else:
    answer = (N // 6) * min_package
    N %= 6
    answer += min(min_each * N, min_package)
    print(answer)
