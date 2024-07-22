A = int(input())
B = int(input())
C = int(input())

zero_list = [0 for _ in range(10)]

ABC = list(map(int, str(A * B * C)))

for i in ABC:
    zero_list[i] += 1

print(*zero_list, sep="\n")