import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(3, N + 1):
    temp_set = set()

    if i % 3 == 0:
        temp_set.add(dp[i // 3] + 1)

    if i % 2 == 0:
        temp_set.add(dp[i // 2] + 1)
    
    temp_set.add(dp[i - 1] + 1)
    
    dp[i] = min(temp_set)

print(dp[N])

# 1 => 0
# 2 => 1
# 3 => 1
# 4 => 2
# 5 => 3
# 6 => 2
# 7 => 3
# 8 => 3
# 9 => 2
# 10 => 3
# 11 => 4
# 12 => 3
# 13 => 4
# 14 => 4
# 15 => 4
