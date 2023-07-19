a = [1,1,2,2,2,8]
b = list(map(int, input().split()))

list(map(lambda x, y: print(x - y, end=" "), a, b))