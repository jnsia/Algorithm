T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    card = input()
    cards = {'S': 13, 'D': 13, 'H': 13, 'C': 13}

    is_error = False
    young_joon = []

    for idx in range(0, len(card), 3):
        cards[card[idx]] -= 1

        tmp_str = ''

        for three in range(3):
            tmp_str += card[idx + three]

        if tmp_str in young_joon:
            is_error = True
            break
        else:
            young_joon.append(tmp_str)

    if is_error:
        print('ERROR')
    else:
        res = []

        for value in cards.values():
            res.append(value)

        print(*res)