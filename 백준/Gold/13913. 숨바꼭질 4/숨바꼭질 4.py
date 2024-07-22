def bfs(start, end):
    queue = deque([[start, [start]]])
    dp = [0] * 100001

    while queue:
        tmp_box = queue.popleft()
        tmp = tmp_box[0]
        tmp_path = tmp_box[1]

        if tmp == end:
            print(dp[end])
            print(*tmp_path)
            break

        if tmp - 1 >= 0 and dp[tmp - 1] == 0:
            dp[tmp - 1] = dp[tmp] + 1
            queue.append([tmp - 1, tmp_path + [tmp - 1]])

        if tmp + 1 < 100001 and dp[tmp + 1] == 0:
            dp[tmp + 1] = dp[tmp] + 1
            queue.append([tmp + 1, tmp_path + [tmp + 1]])

        if tmp * 2 < 100001 and dp[tmp * 2] == 0:
            dp[tmp * 2] = dp[tmp] + 1
            queue.append([tmp * 2, tmp_path + [tmp * 2]])


from collections import deque

N, K = map(int, input().split())

if N <= K:
    bfs(N, K)
else:
    print(N - K)
    
    for num in range(N, K - 1, -1):
        print(num, end=" ")