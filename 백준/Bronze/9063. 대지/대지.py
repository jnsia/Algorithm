N = int(input())

x = []
y = []

for i in range(N):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)

x_len = max(x) - min(x)
y_len = max(y) - min(y)

print(x_len * y_len)