V, E = map(int, input().split())
MAX = float('inf')
city = [[MAX] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    city[a][b] = c

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

answer = MAX

for i in range(1, V + 1):
    cycle = city[i][i]

    if answer > cycle:
        answer = cycle

if answer == MAX:
    print(-1)
else:
    print(answer)
