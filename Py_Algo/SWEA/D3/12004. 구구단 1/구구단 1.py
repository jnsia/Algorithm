def times(n):
    result = False
    
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            result = True
            
    return result

T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    
    N = int(input())
    
    if times(N):
        print('Yes')
    else:
        print('No')