N = int(input())
A = list(map(int, input().split()))

ans = []

for i, v in enumerate(A):
    ans.insert(v, i+1)

print(*reversed(ans))