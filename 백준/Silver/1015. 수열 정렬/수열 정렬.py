N = int(input())
A = list(map(int, input().split()))
count = [0] * 1001
prefix = [0] * 1001
P = [0] * N

for i in range(N):
    count[A[i]] += 1

for i in range(1, 1001):
    prefix[i] = count[i] + prefix[i - 1]

for i in range(N):
    target = A[i]

    P[i] = prefix[target] - count[target]
    count[target] -= 1

print(*P)