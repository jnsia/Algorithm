n = int(input())

result = 0

if n % 4 == 0:
    if n % 100 != 0 or n % 400 == 0:
        result = 1

print(result)