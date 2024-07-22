T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    result = []

    for i in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)

    # 가로 줄 연속된 1의 길이를 찾는다
    for x in range(N):
        count = 0
        for y in range(N):
            if arr[x][y] == 1:
                count += 1
            elif arr[x][y] == 0:
                result.append(count)
                count = 0
        result.append(count)

    # 세로 줄 연속된 1의 길이를 찾는다
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            elif arr[j][i] == 0:
                result.append(count)
                count = 0
        result.append(count)
    
    # 길이가 M인 연속된 1의 시퀀스를 찾는다
    print(f'#{t}', result.count(M))
