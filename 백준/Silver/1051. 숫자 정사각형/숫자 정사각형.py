N, M = map(int, input().split())
board = [input() for _ in range(N)]

answer = 0

for i in range(min(N, M)):
    for j in range(N - i):
        for k in range(M - i):
            if board[j][k] == board[j + i][k] == board[j][k + i] == board[j + i][k + i]:
                answer = max(answer, i + 1)

print(answer * answer)