class Node:
    name = ""
    next = list()


def print_node(node, depth):
    print("--" * depth + node.name)
    node.next.sort(key=lambda x: x.name)

    for next_node in node.next:
        print_node(next_node, depth + 1)


N = int(input())

cave = []

for n in range(N):
    K, *arr = input().split()
    K = int(K)

    now_node = None

    for node in cave:
        if node.name == arr[0]:
            now_node = node
            break

    if not now_node:
        node = Node()
        node.name = arr[0]
        node.next = []
        cave.append(node)
        now_node = node

    for k in range(1, K):
        is_exist = False

        for next_node in now_node.next:
            if next_node.name == arr[k]:
                now_node = next_node
                is_exist = True
                break

        if not is_exist:
            node = Node()
            node.name = arr[k]
            node.next = []
            now_node.next.append(node)
            now_node = node

cave.sort(key=lambda x: x.name)

for node in cave:
    print_node(node, 0)

# print(cave)
