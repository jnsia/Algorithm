C = int(input())

for tc in range(C):
    N, *scores = map(int, input().split())
    avg = sum(scores) / N
    upper_num = 0
    for score in scores:
        if score > avg:
            upper_num += 1
    print(f'{round(upper_num / N * 100, 3)}%')