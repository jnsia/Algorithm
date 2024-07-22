N = int(input())
arr = list(map(int, input().split()))

Y = 0
M = 0

for i in range(N):
    Y += (arr[i] // 30 + 1) * 10
    M += (arr[i] // 60 + 1) * 15

if Y == M:
    print(f"Y M {Y}")
elif Y > M:
    print(f"M {M}")
else:
    print(f"Y {Y}")
