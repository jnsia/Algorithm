T = int(input())

age = []
name = []

for t in range(T):
    N, M = map(str, input().split())
    N = int(N)
    
    age.append([N, M])

age.sort(key=lambda x: x[0])

for j in range(T):
    print(*age[j])