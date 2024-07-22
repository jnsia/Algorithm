N, M = map(int, input().split())

gcd = [1]

for i in range(2, max(N, M) + 1):
    if N % i == 0 and M % i == 0:
        gcd.append(i)

print(max(gcd))

print(int(N * M / max(gcd)))