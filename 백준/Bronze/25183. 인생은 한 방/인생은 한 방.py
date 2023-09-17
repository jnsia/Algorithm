N = int(input())
S = input()
cnt = 1
lotto = False

for idx in range(N - 1):
    if abs(ord(S[idx]) - ord(S[idx + 1])) == 1:
        cnt += 1
    else:
        cnt = 1

    if cnt == 5:
        lotto = True
        break

if lotto:
    print('YES')
else:
    print('NO')