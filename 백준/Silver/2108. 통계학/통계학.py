import sys

N = int(sys.stdin.readline())

lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))

print(round(sum(lst)/len(lst)))

print(sorted(lst)[len(lst)//2])

q_dic = {}

for j in lst:
    q_dic[j] = 0

for k in lst:
    q_dic[k] += 1

most = max(q_dic.values())
max_list = []

for k, v in q_dic.items():
    if v == most:
        max_list.append(k)

if len(max_list) > 1:
    print(sorted(max_list)[1])
else:
    print(max_list[0])

print(max(lst) - min(lst))