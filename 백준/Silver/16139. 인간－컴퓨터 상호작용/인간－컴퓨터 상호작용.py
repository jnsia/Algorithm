import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

dp = [[0 for _ in range(len(S))] for _ in range(26)]

for s in range(len(S)):
    dp[ord(S[s]) - ord('a')][s] = 1

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    cnt = 0

    arr = dp[ord(a) - ord('a')][l: r+1]

    for i in arr:
        if i == 1:
            cnt += 1

    print(cnt)