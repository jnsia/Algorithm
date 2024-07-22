T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    for x in range(N):
        angle_90 = []
        angle_180 = []
        angle_270 = []
        for y in range(N):
            angle_90.append(arr[N - y - 1][x])
            angle_180.append(arr[N - x - 1][N - y - 1])
            angle_270.append(arr[y][N - x - 1])
        print(*angle_90, sep="", end=" ")
        print(*angle_180, sep="", end=" ")
        print(*angle_270, sep="")