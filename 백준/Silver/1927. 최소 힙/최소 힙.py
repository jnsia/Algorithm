import sys
import heapq
input = sys.stdin.readline

N = int(input())

min_heap = []

for n in range(N):
    tmp = int(input())

    if tmp == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, tmp)