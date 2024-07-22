A, B, V = map(int, input().split())

diff = A - B
result = (V - A) / diff + 1

if result == int(result):
    print((V-A) // diff + 1)
else:
    print((V-A) // diff + 2)