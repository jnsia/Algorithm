import sys
input = sys.stdin.readline

M = int(input())
lst = list(map(int, input().split()))

lst.sort()

prev_sum = 0
res = 0

for x in lst:
    res = res + prev_sum + x
    prev_sum = prev_sum + x
    
print(res)