import sys
K, N = map(int, sys.stdin.readline().split())

LANs = [0 for _ in range(K)]
max_len = 0
min_len = 1

for i in range(K):
    LANs[i] = int(sys.stdin.readline())

    if max_len < LANs[i]:
        max_len = LANs[i]

result = 0

while min_len <= max_len:
    count = 0
    mid = (min_len + max_len) // 2
    
    for k in LANs:
        count += k // mid

    if count < N:
        max_len = mid - 1
    elif count >= N:
        min_len = mid + 1
        
        if result <= mid:
            result = mid

print(result)