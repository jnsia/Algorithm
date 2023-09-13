import heapq

N, M, X = map(int, input().split())
attend_adj = [[] for _ in range(N + 1)]
return_adj = [[] for _ in range(N + 1)]
attend_times = [1000000000] * (N + 1)
return_times = [1000000000] * (N + 1)
attend_times[X] = 0
return_times[X] = 0

for _ in range(M):
    s, e, t = map(int, input().split())

    attend_adj[e].append([t, s])
    return_adj[s].append([t, e])

heap = [[0, X]]

while heap:
    time, now = heapq.heappop(heap)

    if time > attend_times[now]:
        continue

    for next_time, not_now in attend_adj[now]:
        if attend_times[not_now] > attend_times[now] + next_time:
            attend_times[not_now] = attend_times[now] + next_time
            heapq.heappush(heap, [attend_times[not_now], not_now])

heap = [[0, X]]

while heap:
    time, now = heapq.heappop(heap)

    if time > return_times[now]:
        continue

    for next_time, not_now in return_adj[now]:
        if return_times[not_now] > return_times[now] + next_time:
            return_times[not_now] = return_times[now] + next_time
            heapq.heappush(heap, [return_times[not_now], not_now])

mx_time = 0

for idx in range(1, N + 1):
    round_time = attend_times[idx] + return_times[idx]

    if round_time > mx_time:
        mx_time = round_time

print(mx_time)