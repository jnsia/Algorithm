N = int(input())
dp = [1] * N
electric_line = []

for _ in range(N):
    a, b = map(int, input().split())
    electric_line.append((a, b))

electric_line.sort(key=lambda s: s[0])

for i in range(N):
    max_len = 0

    for j in range(i, -1, -1):
        if electric_line[i][1] > electric_line[j][1] and dp[j] > max_len:
            max_len = dp[j]

    dp[i] = max_len + 1

# print(electric_line)
# print(dp)
print(N - max(dp))

