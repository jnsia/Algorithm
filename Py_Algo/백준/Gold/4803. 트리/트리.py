def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


case_num = 0

while True:
    case_num += 1
    N, M = map(int, input().split())

    if N == M == 0:
        break

    parent = [_ for _ in range(N + 1)]
    cycle_parent = []

    for _ in range(M):
        a, b = map(int, input().split())

        if find(a) != find(b):
            union(a, b)
        else:
            cycle_parent.append(a)

    print(f'Case {case_num}:', end=" ")

    trees = set()
    cycles = set()

    for idx in range(1, N + 1):
        trees.add(find(parent[idx]))

    for cycle in cycle_parent:
        cycle = find(cycle)
        cycles.add(cycle)

    tree_num = len(trees) - len(cycles)

    if tree_num == 0:
        print('No trees.')
    elif tree_num == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {tree_num} trees.')

