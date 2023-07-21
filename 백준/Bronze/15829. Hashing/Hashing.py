# 순서가 달라져도 출력값은 일정...
L = int(input())
string = input()

r = 0
M = 123456891

alpabet = 'abcdefghijklmnopqrstuvwxyz'

hash_table = {}
H = 0

for i in range(L):
    n = alpabet.index(string[i]) + 1
    r = (31 ** i) % M
    H += n * r

hash_table[string] = H % M

print(hash_table[string])