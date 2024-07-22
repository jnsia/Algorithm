import sys

input = sys.stdin.readline
N, M = map(int, input().split())

one = set()
two = set()

one.update(list(map(int, input().split())))
two.update(list(map(int, input().split())))

three = []
    
three.extend(list(one - two))
three.extend(list(two - one))

print(len(three))
