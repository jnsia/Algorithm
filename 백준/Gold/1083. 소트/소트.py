N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for i in range(N - 1):
    if S == 0:
        break
    
    mx, idx = arr[i], i
    
    for j in range(i + 1, min(N, i + S + 1)):
        if mx < arr[j]:
            mx = arr[j]
            idx = j
    
    S -= idx - i
    
    for j in range(idx, i, -1):
        arr[j] = arr[j - 1]
    
    arr[i] = mx

print(*arr)
