hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def hex_to_dec(hex):
    length = len(hex)
    result = 0

    for digit in range(length):
        result += hex_list.index(hex[digit]) * (16 ** (length - digit - 1))

    return result

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N, K = map(int, input().split())
    hex_num = input()
    quarter = N // 4

    res = []

    for rotate in range(quarter):
        for idx in range(0, N, quarter):
            tmp = ''
            
            for move in range(quarter):
                tmp += hex_num[(idx + rotate + move) % N]
            
            dec = hex_to_dec(tmp)

            if dec not in res:
                res.append(dec)

    print(sorted(res, reverse=True)[K - 1])