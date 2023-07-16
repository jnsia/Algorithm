s = input()
alpabet = {}

for c in range(26):
    alpabet[chr(97 + c)] = -1

for i in range(len(s)):
    a = s.find(s[i])
    alpabet[s[i]] = a

for j in alpabet.values():
    print(j, end=" ")
