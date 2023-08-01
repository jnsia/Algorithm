import sys
input = sys.stdin.readline

S = input()
q = int(input())

for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    dit = dict()

    dit.setdefault(a, 0)

    for k in range(l, r + 1):
        dit.setdefault(S[k], 0)
        dit[S[k]] += 1

    res = dit[a]
    print(res)