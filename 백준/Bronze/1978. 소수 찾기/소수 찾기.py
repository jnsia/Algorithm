def is_prime(n):
    result = True

    if n == 0 or n == 1:
        result = False
    
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if n % i == 0:
            result = False
            break

    return result

N = int(input())
l = list(map(int, input().split()))

count = 0

for j in l:
    if is_prime(j):
        count += 1

print(count)