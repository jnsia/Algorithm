import sys
import heapq
input = sys.stdin.readline

N = int(input())

abs_heap = []

for n in range(N):
    data = int(input())

    if data == 0:
        if len(abs_heap):
            tmp = heapq.heappop(abs_heap)

            if tmp % 2 == 0:
                print(tmp // 2)
            else:
                print(-1 * ((tmp + 1) // 2))
        else:
            print(0)
    else:
        if data > 0:
            heapq.heappush(abs_heap, data * 2)
        else:
            heapq.heappush(abs_heap, -data * 2 - 1)

    # print(abs_heap)
