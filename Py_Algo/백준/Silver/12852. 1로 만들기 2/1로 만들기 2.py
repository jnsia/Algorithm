def bfs(start):
    dp = [0 for _ in range(1000001)]
    queue = deque([[start, [start]]])
    dp[start] = 0

    while queue:
        vertex_set = queue.popleft()
        vertex = vertex_set[0]
        vertex_path = vertex_set[1]

        if vertex == 1:
            print(dp[1])
            print(*vertex_path)
            break

        if vertex % 3 == 0 and dp[vertex // 3] == 0:
            dp[vertex // 3] = dp[vertex] + 1
            queue.append([vertex // 3, vertex_path + [vertex // 3]])

        if vertex % 2 == 0 and dp[vertex // 2] == 0:
            dp[vertex // 2] = dp[vertex] + 1
            queue.append([vertex // 2, vertex_path + [vertex // 2]])

        if vertex - 1 >= 0 and dp[vertex - 1] == 0:
            dp[vertex - 1] = dp[vertex] + 1
            queue.append([vertex - 1, vertex_path + [vertex - 1]])


from collections import deque

N = int(input())

bfs(N)