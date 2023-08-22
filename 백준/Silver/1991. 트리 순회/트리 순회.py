def preorder(node):
    if parents[node]:
        print(node, end="")
        preorder(childs[parents[node]][0])
        preorder(childs[parents[node]][1])


def inorder(node):
    if parents[node]:
        inorder(childs[parents[node]][0])
        print(node, end="")
        inorder(childs[parents[node]][1])


def postorder(node):
    if parents[node]:
        postorder(childs[parents[node]][0])
        postorder(childs[parents[node]][1])
        print(node, end="")


import sys
input = sys.stdin.readline

N = int(input())
parents = dict()
parents['.'] = 0
childs = [['.', '.'] for _ in range(27)]


for idx in range(1, N + 1):
    parent, child1, child2 = input().split()

    parents[parent] = idx
    childs[idx][0] = child1
    childs[idx][1] = child2

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()