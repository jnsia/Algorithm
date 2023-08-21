def play(order):
    global max_score

    score = 0
    turn = 0

    for innings in range(N):
        out_cnt = 0
        b1, b2, b3 = 0, 0, 0

        while True:
            hit = players[innings][order[turn]]

            turn = (turn + 10) % 9

            if hit == 0:
                out_cnt += 1
            elif hit == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            else:
                if hit == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2

                if hit == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1

                if hit == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1

            if out_cnt == 3:
                break

    if score > max_score:
        max_score = score


def perm(depth, res):
    if depth == 9:
        play(res)
        return

    for i in range(9):
        if not ordered[i]:
            if depth > 3:
                ordered[i] = True
                perm(depth + 1, res + [i])
                ordered[i] = False
            else:
                ordered[i] = True
                perm(depth + 1, [i] + res)
                ordered[i] = False


N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]
ordered = [False] * 9
ordered[0] = True
max_score = -1
perm(1, [0])
print(max_score)
