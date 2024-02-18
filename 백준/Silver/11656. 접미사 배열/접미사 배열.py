S = input()
result = []

for i in range(len(S)):
    result.append(S[i:])

print(*sorted(result), sep="\n")