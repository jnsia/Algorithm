import sys
input = sys.stdin.readline

N = 1000 - int(input())
coins = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}

while N > 0:
    for coin in coins.keys():
        if N // coin > 0:
            N -= coin
            coins[coin] += 1
            break

print(sum(coins.values()))