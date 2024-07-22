def bfs(start, end):
    queue = [start]
    num = 0
    dp = [0] * 100001

    while queue:
        num += 1
        for _ in range(len(queue)):
            tmp = queue.pop(0)
            tmp_list = [tmp + 1, tmp - 1, tmp * 2]

            for i in tmp_list:
                if 0 <= i < 100001:
                    if dp[i] == 0:
                        dp[i] = num
                        queue.append(i)

        if dp[end]:
            return dp[K]


N, K = map(int, input().split())

if N == K:
    print(0)
else:
    print(bfs(N, K))
