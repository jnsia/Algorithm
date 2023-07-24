T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())
    
    apart = [[0 for _ in range(n)] for _ in range(k + 1)]
    apart[0] = list(range(1, n + 1))
    
    for i in range(1, k + 1):
        for j in range(n):
            for p in range(j + 1):
                apart[i][j] += apart[i-1][p]
    
    print(apart[k][n - 1])