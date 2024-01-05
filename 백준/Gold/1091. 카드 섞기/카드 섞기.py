def check():
    flag = True

    for i in range(N):
        if P[i] != i % 3:
            flag = False

    return flag


def suffle():
    nP = P[:]

    for i in range(N):
        ni = S[i]
        nP[ni] = P[i]

    return nP

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

answer = 0

while answer < 1000000:
    if check():
        break

    P = suffle()
    answer += 1

if answer == 1000000:
    print(-1)
else:
    print(answer)
