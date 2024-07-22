def prime(n, m):
    for i in range(n, m + 1):
        res = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                res = False
                break
        if res and i > 1:
            print(i)
        
N, M = map(int, input().split())

prime(N, M)
