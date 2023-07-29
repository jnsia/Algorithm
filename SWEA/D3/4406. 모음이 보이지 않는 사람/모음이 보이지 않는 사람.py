T = int(input())

aeiou = 'aeiou'

for t in range(1, T + 1):
    print(f'#{t}', end=" ")

    S = input()

    new_str = ''

    for s in S:
        if s not in aeiou:
            new_str += s
            
    print(new_str)