def dfs(node):
    global answer

    if node == K:
        return

    is_leaf = True

    for next_node in range(N):
        if arr[next_node] == node and not next_node == K:
            dfs(next_node)
            is_leaf = False

    if is_leaf:
        answer += 1


N = int(input())
arr = list(map(int, input().split()))
K = int(input())

answer = 0

root = 0

for i in range(N):
    if arr[i] == -1:
        root = i

dfs(root)
print(answer)
