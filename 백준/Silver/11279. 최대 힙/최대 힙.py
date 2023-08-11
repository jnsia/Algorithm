import sys
import heapq
input = sys.stdin.readline

N = int(input())

max_heap = []

for n in range(N):
    tmp = int(input())

    if tmp == 0:
        if len(max_heap):
            print(-1 * heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -tmp)