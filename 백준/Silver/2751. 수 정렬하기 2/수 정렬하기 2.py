import sys

N = int(input())
numbers = []

for i in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for j in numbers:
    print(j)