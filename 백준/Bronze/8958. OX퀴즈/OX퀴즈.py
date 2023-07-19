T = int(input())

def ox(string):
    result = 0
    count = 1
    prev = 'X'

    for i in string:
        if i == 'O':
            if prev == i:
                count += 1

            result += count
            prev = 'O'
        else:
            prev = 'X'
            count = 1

    return result

for _ in range(T):
    S = input()
    print(ox(S))