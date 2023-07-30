import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

P = 'I'

for i in range(N):
    P = 'IO' + P

cnt = 0

for j in range(M - len(P) + 1):
    if P == S[j:j+len(P)]:
        cnt += 1

print(cnt)