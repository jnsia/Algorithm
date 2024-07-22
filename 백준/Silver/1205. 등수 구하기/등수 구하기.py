# 10 <= P <= 50
# 0 <= N <= P

N, S, P = map(int, input().split())
ranking = [-1] * P

if N > 0:
    scores = list(map(int, input().split()))

    for i in range(N):
        ranking[i] = scores[i]

answer = -1
count = 0

for i in range(P):
    if S > ranking[i]:
        answer = i + 1 - count
        break
    elif S == ranking[i]:
        count += 1
    else:
        count = 0

print(answer)