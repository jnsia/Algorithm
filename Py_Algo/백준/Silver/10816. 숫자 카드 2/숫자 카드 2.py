import sys

N_dict = {}

N = int(sys.stdin.readline())
N_numbers = list(map(int, sys.stdin.readline().split()))
N_set = set(N_numbers)

for k in N_set:
    N_dict[k] = 0

for j in N_numbers:
    N_dict[j] += 1

M = int(sys.stdin.readline())
M_numbers = list(map(int, sys.stdin.readline().split()))

result = [0] * M

for i, v in enumerate(M_numbers):
    if v in N_set:
        result[i] = N_dict[v]
    else:
        result[i] = 0

print(*result, end=" ")