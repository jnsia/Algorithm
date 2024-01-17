N = int(input())
current = input()
target = input()

dp = [[[float('inf') for _ in range(10)] for _ in range(2)] for _ in range(N)]

current_num = int(current[0])
target_num = int(target[0])

diff = target_num - current_num

dp[0][0][(10 + diff) % 10] = (10 + diff) % 10
dp[0][1][0] = (10 - diff) % 10

idx = 1

while idx < N:
    current_num = int(current[idx])
    target_num = int(target[idx])

    diff = target_num - current_num

    for i in range(10):
        tmp = ((target_num - i + 10) % 10 - current_num)
        dp[idx][0][(10 + diff) % 10] = min(dp[idx][0][(10 + diff) % 10],
                                           dp[idx - 1][0][i] + (10 + tmp) % 10,
                                           dp[idx - 1][1][i] + (10 + tmp) % 10)
        dp[idx][1][i] = min(dp[idx][1][i],
                            dp[idx - 1][0][i] + (10 - tmp) % 10,
                            dp[idx - 1][1][i] + (10 - tmp) % 10)

    idx += 1

answer = float('inf')

for i in range(10):
    answer = min(answer, dp[N - 1][0][i], dp[N - 1][1][i])

print(answer)