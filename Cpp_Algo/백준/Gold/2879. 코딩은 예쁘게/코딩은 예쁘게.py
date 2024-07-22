N = int(input())
taps = list(map(int, input().split()))
corrects = list(map(int, input().split()))

differences = [0] * N

for i in range(N):
    differences[i] = taps[i] - corrects[i]

dp = [0] * N

prev = differences[0]

if prev >= 0:
    is_positive = True
else:
    is_positive = False

for i in range(1, N):
    difference = prev - differences[i]

    if is_positive:
        if differences[i] <= 0:
            is_positive = False
            dp[i - 1] = prev
            prev = differences[i]
        elif difference >= 0:
            dp[i - 1] = difference
    else:
        if differences[i] >= 0:
            is_positive = True
            dp[i - 1] = -prev
            prev = differences[i]
        elif difference <= 0:
            dp[i - 1] = -difference

    # print(i, dp)
    prev = differences[i]

dp[N - 1] = abs(prev)

# print(differences)
# print(dp)
print(sum(dp))