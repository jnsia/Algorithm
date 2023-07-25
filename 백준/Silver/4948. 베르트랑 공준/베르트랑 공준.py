import sys

input = sys.stdin.readline

def countPrime(n, m):
    cnt = 0
    prime_list = [True] * (m + 1)

    r = int(m ** 0.5)

    for i in range(2, r + 1):
        if prime_list[i] == True:
            for j in range(i+i, m + 1, i):
                prime_list[j] = False

    for k in range(n, m + 1):
        if prime_list[k] == True:
            cnt += 1

    return cnt

while True:
    N = int(input())

    if N == 0:
        break

    print(countPrime(N + 1, N * 2))
