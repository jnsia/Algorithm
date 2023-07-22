N = int(input())

i = 2

while N > 1:
    if N % i == 0:
        N = N / i
        print(i)
        i = 1
    
    i += 1