T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())

    bus_stop = [0] * 5001

    for i in range(N):
        Ai, Bi = map(int, input().split())
        
        for k in range(Ai, Bi + 1):
            bus_stop[k] += 1

    P = int(input())
    
    for j in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()