# 30 이하
N = int(input())
# 500 이하
weights = list(map(int, input().split()))
# 7 이하
M = int(input())
# 40000 이하
balls = list(map(int, input().split()))

MAX_weight = min(sum(weights) + 1, 40001)

dp = [[0] * MAX_weight for _ in range(N + 1)]

for i in range(1, N + 1):
    weight = weights[i - 1]

    for j in range(1, MAX_weight):
        if j >= weight:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + weight)
        else:
            dp[i][j] = dp[i - 1][j]

answer = []

for w in dp[N]:
    if w not in answer:
        answer.append(w)

# print(dp)

for i in range(M):
    ball = balls[i]
    flag = False

    for j in answer:
        temp = ball + j

        if temp in answer:
            flag = True
            break

    if flag:
        print('Y', end=" ")
    else:
        print('N', end=" ")

