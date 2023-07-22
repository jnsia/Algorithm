import sys

N = int(sys.stdin.readline())
N_numbers = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_numbers = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if M_numbers[i] in N_numbers:
        print(1)
    else:
        print(0)