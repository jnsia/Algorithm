import sys
input = sys.stdin.readline

S = input().strip().split('-')

min_sum = 0

for i in S[0].split('+'):
    min_sum += int(i)

for n in S[1:]:
    tmp_sum = 0
    for m in n.split('+'):
        tmp_sum += int(m)
    min_sum -= tmp_sum

# print(S)
print(min_sum)