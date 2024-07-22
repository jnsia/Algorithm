T = int(input())

for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    
    L, U, X = map(int, input().split())

    if L <= X <= U:
        print(0)
    elif X > U:
        print(-1)
    else:
        print(L - X)    
    