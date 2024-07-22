def gcd(a, b):
    if b == 0:
        return a
    elif a < b:
        a, b  = b, a
    elif a % b == 0:
        return b
    
    return gcd(b, a % b)

import sys
input = sys.stdin.readline

N = int(input())

trees = set()
distances = set()

prev = None
start = 0
end = 0

for i in range(N):
    tree = int(input())
    trees.add(tree)
    
    if prev == None:
        prev = tree
        start = tree
    else:
        distance = tree - prev
        distances.add(distance)
        prev = tree
        end = tree
        
distances = list(distances)
distances.sort()

if len(distances) == 1:
    diff = distances[0]
elif distances[0] == 1:
    diff = 1
else:
    while len(distances) > 1:
        diff = gcd(distances[0], distances[1])
        del distances[0]
        distances.append(diff)
        del distances[0]

cnt = (end - start) // diff - len(trees) + 1

print(cnt)