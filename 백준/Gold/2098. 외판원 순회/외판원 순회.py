def tsp(node, visited):
    if visited == END:
        if matrix[node][0]:
            return matrix[node][0]
        return float('inf')

    if cost_list[node][visited]:
        return cost_list[node][visited]

    cost_list[node][visited] = MAX

    for next_node in range(N):
        if matrix[node][next_node] == 0:
            continue

        if visited & (1 << next_node):
            continue

        temp = tsp(next_node, visited | 1 << next_node)
        cost_list[node][visited] = min(cost_list[node][visited], matrix[node][next_node] + temp)

    return cost_list[node][visited]


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
cost_list = [[0] * (1 << N) for _ in range(N)]
MAX = float('inf')
END = (1 << N) - 1

print(tsp(0, 1))
