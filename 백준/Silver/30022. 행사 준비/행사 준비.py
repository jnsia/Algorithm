N, A, B = map(int, input().split())
p = [0] * N
q = [0] * N
diff = [[0, 0] for _ in range(N)]

for idx in range(N):
    pi, qi = map(int, input().split())
    p[idx] = pi
    q[idx] = qi
    diff[idx] = [(pi - qi), idx]

diff.sort()

answer = 0

for idx in range(A):
    answer += p[diff[idx][1]]

for idx in range(A, N):
    answer += q[diff[idx][1]]

print(answer)
