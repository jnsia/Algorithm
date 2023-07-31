import sys

input = sys.stdin.readline

N, M = map(int, input().split())

coin = [0] * N

for n in range(N):
    coin[n] = int(input())

coin.sort(reverse=True)
cnt = 0

while M > 0:
    for i in coin:
        if M // i:
            cnt += M // i
            M -= i * (M // i)
            break
print(cnt)

