N, K = map(int, input().split())
dolls = list(map(int, input().split()))
ryan = 0
apeach = 0
mn_len = 1000001

i = 0
j = 1

if dolls[0] == 1:
    ryan += 1
else:
    apeach += 1

while i < j:
    if j >= N:
        if dolls[i] == 1:
            ryan -= 1
        else:
            apeach -= 1

        i += 1

        if ryan == K:
            if mn_len > j - i:
                mn_len = j - i

        continue

    if ryan == K:
        if mn_len > j - i:
            mn_len = j - i

        if dolls[i] == 1:
            ryan -= 1
        else:
            apeach -= 1

        i += 1
    elif ryan < K:
        if dolls[j] == 1:
            ryan += 1
        else:
            apeach += 1

        j += 1
    else:
        if dolls[i] == 1:
            ryan -= 1
        else:
            apeach -= 1

        i += 1

if mn_len == 1000001:
    print(-1)
else:
    print(mn_len)