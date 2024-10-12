def search(num, like_nums):
    results = []

    for x in range(N):
        for y in range(N):
            if class_room[x][y]: continue

            like_count = 0
            blank_count = 0

            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]

                if nx < 0 or nx >= N: continue
                if ny < 0 or ny >= N: continue

                if class_room[nx][ny] == 0:
                    blank_count += 1

                if class_room[nx][ny] in like_nums:
                    like_count += 1

            results.append((like_count, blank_count, x, y))

    results.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    result = results[0]
    class_room[result[2]][result[3]] = num


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
like_students = [[] for _ in range(N * N + 1)]
class_room = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N * N):
    arr = list(map(int, input().split()))
    search(arr[0], arr[1:])
    like_students[arr[0]].extend(arr[1:])

answer = 0

for x in range(N):
    for y in range(N):
        like_count = 0

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue

            if class_room[nx][ny] in like_students[class_room[x][y]]:
                like_count += 1

        if like_count:
            answer += 10 ** (like_count - 1)

print(answer)