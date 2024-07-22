import heapq

T = int(input())

for tc in range(1, T + 1):
    K = int(input())

    deleted = [True] * K
    min_heap = []
    max_heap = []

    for idx in range(K):
        cmd, data = map(str, input().split())
        data = int(data)

        if cmd == 'I':
            heapq.heappush(min_heap, (data, idx))
            heapq.heappush(max_heap, (-data, idx))
            deleted[idx] = False

        elif cmd == 'D':
            if data == -1:

                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)

            if data == 1:

                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
    
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        mn = heapq.heappop(min_heap)
        mx = heapq.heappop(max_heap)
        
        print(-mx[0], mn[0])
    else:
        print('EMPTY')
