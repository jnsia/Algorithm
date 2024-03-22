N = int(input())

arr = []

for i in range(N):
    temp = input().split()
    arr.append(temp)

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(arr[i][0])
