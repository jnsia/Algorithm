N = int(input())

res = 1

for i in range(1, N + 1):
    if N == 0:
        res = 1
        break
    else:
        res *= i

print(res)