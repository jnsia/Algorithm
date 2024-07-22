T = int(input())

for t in range(1, T + 1):
    print(f'#{t}')
    N = int(input())

    x = 1
    a = [0, 1]
    print(1)

    for i in range(N - 1):
        x += 1
        ar = a[:]
        for j in range(1, x):
            a[j] = ar[j - 1] + ar[j]
        a.append(1)
        
        for k in range(1, len(a)):
            print(a[k], end=" ")
        print()