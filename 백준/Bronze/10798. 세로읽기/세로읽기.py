zero_map = [['' for _ in range(16)] for _ in range(5)]
numbers_map = [list(input()) for _ in range(5)]

result = ''

for x in range(5):
    for y in range(len(numbers_map[x])):
        zero_map[x][y] = numbers_map[x][y]

for i in range(16):
    for j in range(5):
        result += zero_map[j][i]

print(result)