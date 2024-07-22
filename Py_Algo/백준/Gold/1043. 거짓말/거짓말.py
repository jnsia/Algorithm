def union(x, y):
    x = find_comp(x)
    y = find_comp(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find_comp(z):
    if parent[z] == z:
        return z

    parent[z] = find_comp(parent[z])
    return parent[z]

N, M = map(int, input().split())
truth_num, *truth_people = list(map(int, input().split()))
parent = [num for num in range(N + 1)]
rank = []
party_arr = []
root = 0

if truth_num:
    root = min(truth_people)

for person in truth_people:
    union(root, person)

for _ in range(M):
    num, *people = list(map(int, input().split()))
    party_root = min(people)
    party_root = find_comp(party_root)

    for person in people:
        union(party_root, person)

    party_arr.append(people)

if not root:
    print(M)
else:
    cnt = 0

    for party in party_arr:
        is_possible = True

        for person in party:
            if find_comp(root) == find_comp(parent[person]):
                is_possible = False
                break

        if is_possible:
            cnt += 1

    print(cnt)
