import sys
input = sys.stdin.readline

def dfs(graph, start):
    visited = set()
    stack = [start]
    route = []

    while stack:
        vertex = stack.pop()
        stack.extend(reversed(graph[vertex]))

        if vertex not in visited:
            visited.add(vertex)
            route.append(vertex)

    return route

T = int(input())

for t in range(T):
    N = int(input())

    node_dict = {}

    for n in range(1, N):
        A, B = map(int, input().split())
        node_dict.setdefault(n, [])
        node_dict.setdefault(B, [])
        node_dict[B].append(A)

    x, y = map(int, input().split())
    # print(node_dict)

    x_route = dfs(node_dict, x)
    y_route = dfs(node_dict, y)

    for i in x_route:
        if i in y_route:
            print(i)
            break
