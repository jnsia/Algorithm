# 순서가 달라져도 출력값은 일정...
L = int(input())
string = input()

r = 31
M = 123456891

alpabet = 'abcdefghijklmnopqrstuvwxyz'

hash_table = {}
H = 0

for i in range(L):
    n = alpabet.index(string[i]) + 1
    H += (n) * (31 ** i)

hash_table[string] = H % M

print(hash_table[string])