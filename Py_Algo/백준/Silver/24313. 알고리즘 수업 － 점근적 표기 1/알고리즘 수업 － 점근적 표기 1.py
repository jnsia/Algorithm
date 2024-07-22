a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = 1

for n in range(n0, 101):
    fn = a1 * n + a0
    
    if fn > c * n:
        result = 0

print(result)