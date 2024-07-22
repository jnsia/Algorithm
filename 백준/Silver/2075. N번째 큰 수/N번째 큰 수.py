import heapq

MIN = -1000000001

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

indexes = [N - 1] * N
heap = []

while len(heap) < N:
    max_value = MIN
    max_index = -1

    for col in range(N):
        row = indexes[col]
        value = board[row][col]

        if max_value < value:
            max_value = value
            max_index = col

    indexes[max_index] -= 1
    heapq.heappush(heap, max_value)

print(heapq.heappop(heap))