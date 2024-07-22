def dfs(idx, line):
    global mx_crush

    new_line = line[:]

    if idx == N:
        tmp = 0

        for a, b in new_line:
            if a <= 0:
                tmp += 1

        if mx_crush < tmp:
            mx_crush = tmp

        return

    if new_line[idx][0] <= 0:
        dfs(idx + 1, new_line)
        return

    for other in range(N):
        if idx != other:
            if new_line[other][0] > 0:
                new_line[idx][0] -= new_line[other][1]
                new_line[other][0] -= new_line[idx][1]
                dfs(idx + 1, new_line)
                new_line[idx][0] += new_line[other][1]
                new_line[other][0] += new_line[idx][1]
            else:
                dfs(idx + 1, new_line)

N = int(input())
eggs = []
mx_crush = 0

for _ in range(N):
    S, W = map(int, input().split())
    eggs.append([S, W])

dfs(0, eggs)
print(mx_crush)