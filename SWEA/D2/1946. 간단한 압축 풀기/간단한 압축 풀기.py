T = int(input())

for t in range(1, T + 1):
    print(f'#{t}')

    N = int(input())
    str_list = []

    for i in range(N):
        n, m = map(str, input().split())
    
        for j in range(int(m)):
            str_list.append(n)

    while len(str_list) > 0:
        for k in range(10):
            if len(str_list) != 0:
                print(str_list[0], end="")
                del str_list[0]
            else:
                break
        print()