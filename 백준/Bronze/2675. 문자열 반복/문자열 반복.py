T = int(input())

for i in range(T):
    R, S = input().split()
    a = list(map(lambda x: x * int(R), S))
    print(*a, sep="")