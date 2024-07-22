DNA = 'ACGT'
num = [0, 0, 0, 0]

S, P = map(int, input().split())
sequence = input()
min_num = list(map(int, input().split()))
answer = 0

for i in range(P):
    word = sequence[i]
    num[DNA.index(word)] += 1

is_true = True

for i in range(4):
    if min_num[i] > num[i]:
        is_true = False
        break

if is_true:
    answer += 1

for i in range(S - P):
    word = sequence[i]
    num[DNA.index(word)] -= 1
    word = sequence[P + i]
    num[DNA.index(word)] += 1

    is_true = True

    for i in range(4):
        if min_num[i] > num[i]:
            is_true = False
            break

    if is_true:
        answer += 1

print(answer)