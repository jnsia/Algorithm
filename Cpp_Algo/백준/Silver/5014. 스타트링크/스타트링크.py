from collections import deque

# 최대 F층 / 현재 위치 S층 / 목적지 G층 / 위로 U층 이동 가능 / 아래로 D층 이동 가능
F, S, G, U, D = map(int, input().split())
visited = [1000001] * (F + 1)
visited[S] = 0

queue = deque()
queue.append(S)

while queue:
    now = queue.popleft()

    if (now + U) < (F + 1) and visited[now + U] == 1000001:
        queue.append(now + U)
        visited[now + U] = visited[now] + 1

    if (now - D) > 0 and visited[now - D] == 1000001:
        queue.append(now - D)
        visited[now - D] = visited[now] + 1

if visited[G] == 1000001:
    print("use the stairs")
else:
    print(visited[G])
