import sys
input = sys.stdin.readline

N = int(input())

dp = [4] * 50001

n = int(50000 ** 0.5)

square_list = list()
square_list2 = list()

for i in range(1, n + 1):
    i_sqr = i ** 2
    dp[i_sqr] = 1
    square_list.append(i_sqr)

for j in square_list:
    for k in square_list:
        if j + k < 50001 and dp[j + k] == 4:
            dp[j + k] = 2
            square_list2.append(j + k)

for l in square_list:
    for m in square_list2:
        if l + m < 50001 and dp[l + m] == 4:
            dp[l + m] = 3

print(dp[N])