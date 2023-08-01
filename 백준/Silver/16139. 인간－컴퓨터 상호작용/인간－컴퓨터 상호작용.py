import sys
input = sys.stdin.readline

S = input()
q = int(input())

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    res = S[l:r+1].count(a)
    print(res)