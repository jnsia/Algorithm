import math

N = int(input())

for i in range(N):
    r, n = map(int, input().split())

    res = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    print(res)