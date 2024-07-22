T = int(input())

for t in range(1, T + 1):
    S = input()
    print(f'#{t}', end=" ")

    orev = ''
    cnt = 0

    for i in S:
        if i == '|' and orev == '(':
            cnt += 1
        elif i == ')' and orev == '(':
            cnt += 1
        elif i == ')' and orev == '|':
            cnt += 1
        
        orev = i

    print(cnt)