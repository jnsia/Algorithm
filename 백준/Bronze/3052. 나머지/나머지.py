l = []

for x in range(10):
    n = int(input())
    l.append(n % 42)

l = set(l)
print(len(l))