players, numbers = map(int, input().split())
rooms = [[] for _ in range(300)]
enter_level = [0] * 300

for _ in range(players):
    level, nickname = input().split()
    level = int(level)

    for i in range(300):
        if len(rooms[i]) < numbers and (abs(enter_level[i] - level) <= 10 or enter_level[i] == 0):
            rooms[i].append((level, nickname))

            if len(rooms[i]) == 1:
                enter_level[i] = level

            break

for i in range(300):
    if enter_level[i] > 0:
        rooms[i].sort(key=lambda x: x[1])

        if len(rooms[i]) == numbers:
            print("Started!")

            for j in range(len(rooms[i])):
                print(*rooms[i][j])
        else:
            print("Waiting!")

            for j in range(len(rooms[i])):
                print(*rooms[i][j])

