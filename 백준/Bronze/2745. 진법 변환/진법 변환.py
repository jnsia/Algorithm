B = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
S, N = input().split()

reversed_list = list(S)[::-1]

result = 0

for idx, value in enumerate(reversed_list):
    result += B.index(value) * (int(N) ** idx)

print(result)