import sys
input = sys.stdin.readline

K, L = map(int, input().split())

waits = dict()

for i in range(1, L + 1):
    number = input()

    waits[number] = i

arr = list()

for k, v in waits.items():
    arr.append((k, v))

arr.sort(key=lambda x: x[1])

for i in range(min(len(arr), K)):
    print(arr[i][0], end="")