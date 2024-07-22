N = int(input())
solutions = sorted(list(map(int, input().split())))

value = solutions[0] + solutions[N - 1]
optimal = value

base = 0
acid = N - 1

answer = (solutions[0], solutions[N - 1])

while base < acid - 1:
    if value == 0:
        optimal = 0
        answer = (solutions[base], solutions[acid])
        break

    if value < 0:
        value -= solutions[base]
        base += 1
        value += solutions[base]
    else:
        value -= solutions[acid]
        acid -= 1
        value += solutions[acid]

    if abs(value) < abs(optimal):
        optimal = value
        answer = (solutions[base], solutions[acid])

print(*answer)
