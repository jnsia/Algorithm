def dfs(idx, cnt):
    if idx == N:
        if cnt != M:
            return 

        for i in range(N):
            if bits[i] == 1:
                print(numbers[i], end=" ")
        print()
        return

    bits[idx] = 1
    dfs(idx + 1, cnt + 1)
    bits[idx] = 0
    dfs(idx + 1, cnt)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
bits = [0] * N
dfs(0, 0)