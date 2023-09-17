import heapq

N, M = map(int, input().split())
cards = list(map(int, input().split()))
heap = []

for card in cards:
    heapq.heappush(heap, card)

for _ in range(M):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)

    z = x + y

    heapq.heappush(heap, z)
    heapq.heappush(heap, z)

print(sum(heap))