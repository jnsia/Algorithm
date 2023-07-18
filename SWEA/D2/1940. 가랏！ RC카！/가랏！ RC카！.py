T = int(input())

for t in range(1, T + 1):
    N = int(input())

    speed = 0
    distance = 0
    
    for i in range(N):
        n = list(map(int, input().split()))

        if n[0] == 1:
            speed += n[1]
        elif n[0] == 2:
            if speed > 0:
                speed -= n[1]

        distance += speed
            
    print(f'#{t}', end=" ")
    print(distance)
