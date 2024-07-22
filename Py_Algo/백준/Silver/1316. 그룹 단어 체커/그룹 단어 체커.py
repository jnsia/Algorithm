def is_group(string):
    group_dic = {}
    result = True
    prev = ''

    for j in string:
        group_dic[j] = 0

    for i in string:
        if i == prev:
            continue
        elif group_dic[i] == 1:
            result = False
        else:
            group_dic[i] = 1

        prev = i


    return result

N = int(input())

count = 0

for i in range(N):
    S = input()
    if is_group(S):
        count += 1

print(count)