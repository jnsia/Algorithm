S = input().upper()

l = [0 for _ in range(26)]

for i in S:
    l[ord(i) - 65] += 1

max_num = max(l)

if l.count(max_num) != 1:
    print('?')
else:
    print(chr(l.index(max_num) + 65))