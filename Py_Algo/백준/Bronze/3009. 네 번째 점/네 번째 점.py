a = []
b = []

for i in range(3):
    n, m = map(int, input().split())

    if n in a:
        a.remove(n)
    else:
        a.append(n)

    if m in b:
        b.remove(m)
    else:
        b.append(m)

print(*a, *b)