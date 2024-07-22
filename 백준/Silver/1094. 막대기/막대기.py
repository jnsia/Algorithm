import sys
input = sys.stdin.readline

N = int(input())
binary = ""

while N > 0:
    binary += str(N % 2)
    N //= 2

print(binary.count('1'))