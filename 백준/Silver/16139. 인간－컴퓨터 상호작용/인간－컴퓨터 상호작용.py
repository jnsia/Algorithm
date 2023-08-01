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

    res = dp[ord(a) - ord('a')][l:r+1].count(1)
    print(res)