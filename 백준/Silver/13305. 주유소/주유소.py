import sys
input = sys.stdin.readline

N = int(input())
road_len = list(map(int, input().split()))
oil_price= list(map(int, input().split()))

cost = 0
min_price = oil_price[0]

for i in range(N - 1):
    cost += min_price * road_len[i]

    if min_price > oil_price[i + 1]:
        min_price = oil_price[i + 1]

print(cost)