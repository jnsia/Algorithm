N, M = map(int, input().split())

A_list = []
B_list = []

for _ in range(N):
    A = list(map(int, input().split()))
    A_list.append(A)

M, K = map(int, input().split())

for _ in range(M):
    B = list(map(int, input().split()))
    B_list.append(B)

dp = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for k in range(K):
        tmp_sum = 0
        for j in range(M):
            tmp_sum += A_list[i][j] * B_list[j][k]
        dp[i][k] = tmp_sum

for output in dp:
    print(*output)