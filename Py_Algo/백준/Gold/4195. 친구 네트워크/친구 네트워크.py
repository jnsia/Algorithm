def convert_name_to_id(name):
    global index

    if name in id_dict:
        return id_dict.get(name)
    else:
        index += 1
        id_dict[name] = index
        return index

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[x] = y
        cnt_list[y] += cnt_list[x]

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [i for i in range(200000)]
    id_dict = {}
    index = -1
    cnt = 0
    cnt_list = [1 for _ in range(200000)]

    for _ in range(N):
        name1, name2 = input().rstrip().split()

        a = convert_name_to_id(name1)
        b = convert_name_to_id(name2)

        union(a, b)
        ans = cnt_list[find(a)]
        print(ans)
