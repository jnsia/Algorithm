def dfs():
    visited = [False] * (N + 1)
    visited[1] = True
    stack = [1]

    while stack:
        vertex = stack.pop()

        for nv in adj_list[vertex]:
            if visited[nv] == False:
                visited[nv] = True
                par_list[nv] = vertex
                stack.append(nv)


N = int(input())

adj_list = [[] for _ in range(N + 1)]
par_list = [0] * (N + 1)

for _ in range(N - 1):
    v1, v2 = map(int, input().split())

    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

dfs()
print(*par_list[2:], sep="\n")
