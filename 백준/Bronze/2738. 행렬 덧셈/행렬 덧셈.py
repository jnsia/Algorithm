N, M = map(int, input().split())

first_map = [[x for x in list(map(int, input().split()))] for _ in range(N)]
second_map = [[y for y in list(map(int, input().split()))] for _ in range(N)]

for i in range(N):
    for j in range(M):
        first_map[i][j] += second_map[i][j]

for k in first_map:
    print(*k)