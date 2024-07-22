import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

s = min(N_list) * max(N_list)
print(s)