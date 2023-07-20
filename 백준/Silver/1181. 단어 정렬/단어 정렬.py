N = int(input())

strings = []

for i in range(N):
    strings.append(input())

result = []
strings = list(set(strings))
strings.sort()

i = 1

while True:
    for s in strings:
        if len(s) == i:
            result.append(s)

    if len(result) == len(strings):
        break

    i += 1

print(*result, sep='\n')