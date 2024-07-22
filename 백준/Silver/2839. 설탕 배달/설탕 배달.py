N = int(input())

cnt = 0

while N > 5:
    if N % 5 != 0:
        N -= 3
        cnt += 1
    else:
        N -= 5
        cnt += 1

if N == 5 or N == 3:
    cnt += 1
else:
    cnt = -1

print(cnt)