# def set_child(parent, child):
#     if parent > child:
#         if tree[parent][0] == 0:
#             tree[parent][0] = child
#             return
#         else:
#             set_child(tree[parent][0], child)
#     else:
#         if tree[parent][1] == 0:
#             tree[parent][1] = child
#             return
#         else:
#             set_child(tree[parent][1], child)

class node:
    def __init__(self, data):
        self.data = data
        self.next = [None, None]

class tree:
    def __init__(self):
        self.root = None

# def postorder(vertex):
#     if tree[vertex][0]:
#         postorder(tree[vertex][0])
#
#     if tree[vertex][1]:
#         postorder(tree[vertex][1])
#
#     print(vertex)

def postorder(vertex: node):
    if vertex.next[0]:
        postorder(vertex.next[0])

    if vertex.next[1]:
        postorder(vertex.next[1])

    print(vertex.data)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# tree = [[0, 0] for _ in range(1000001)]
trees = tree()
trees.root = node(int(input().strip()))

try:
    while True:
        num = int(input().strip())
        now_node = trees.root
        while True:
            next_idx = 0

            if now_node.data < num:
                next_idx = 1

            if now_node.next[next_idx] == None:
                now_node.next[next_idx] = node(num)
                break
            else:
                now_node = now_node.next[next_idx]
        # set_child(root_node, node)
except:
    postorder(trees.root)
