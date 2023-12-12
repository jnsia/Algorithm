def dfs(node):
    times = []

    for n in range(N):
        if node == parent[n]:
            dfs(n)
            times.append(answer[n])

    times.sort()

    for idx in range(len(times)):
        times[idx] -= idx
        if times[idx] < 0:
            times[idx] = 0

    answer[node] = len(times)

    if times:
        answer[node] += max(times)


N = int(input())
parent = list(map(int, input().split()))
answer = [0] * N

dfs(0)

print(answer[0])