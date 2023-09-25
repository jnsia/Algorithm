def find(elem):
	if island[elem] == elem:
		return elem

	island[elem] = find(island[elem])
	return island[elem]


def union(x, y):
	x = find(x)
	y = find(y)

	if x > y:
		island[x] = y
	else:
		island[y] = x


def check_bridge(x, y, num):
	for move in range(4):
		go = 1

		while True:
			nx = x + dx[move] * go
			ny = y + dy[move] * go

			if 0 <= nx < N and 0 <= ny < M:
				if country[nx][ny] == 0:
					go += 1
				elif country[nx][ny] != num and go > 2:
					heapq.heappush(bridge_list, (go - 1, num, country[nx][ny]))
					break
				else:
					break
			else:
				break


def check_island(sx, sy, num):
	queue = deque([(sx, sy)])

	while queue:
		x, y = queue.popleft()

		for move in range(4):
			nx = x + dx[move]
			ny = y + dy[move]

			if 0 <= nx < N and 0 <= ny < M and country[nx][ny] == 1:
				country[nx][ny] = num
				queue.append((nx, ny))


import heapq
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
island_num = 2

for i in range(N):
	for j in range(M):
		if country[i][j] == 1:
			country[i][j] = island_num
			check_island(i, j, island_num)
			island_num += 1

bridge_list = []

island = [_ for _ in range(island_num)]

for i in range(N):
	for j in range(M):
		if country[i][j]:
			check_bridge(i, j, country[i][j])

total_cost = 0
connect_num = 0

while bridge_list:
	cost, start, end = heapq.heappop(bridge_list)

	if find(start) != find(end):
		connect_num += 1
		total_cost += cost
		union(start, end)


if island_num > connect_num + 3:
	print(-1)
else:
	print(total_cost)