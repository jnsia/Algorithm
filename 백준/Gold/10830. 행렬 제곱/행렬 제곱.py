def matrix_times(matrix1, matrix2):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += matrix1[i][k] * matrix2[k][j]
            result[i][j] = temp % 1000

    return result


def power(matrix, sqr):
    if sqr == 1:
        return early_matrix

    if sqr == 2:
        return matrix_times(early_matrix, early_matrix)

    if sqr % 2:
        sqr_matrix = power(matrix, sqr - 1)
        return matrix_times(sqr_matrix, early_matrix)
    else:
        sqr_matrix = power(matrix, sqr // 2)
        return matrix_times(sqr_matrix, sqr_matrix)


N, B = map(int, input().split())
early_matrix = [list(map(int, input().split())) for _ in range(N)]

ans = power(early_matrix, B)

for row in range(N):
    for col in range(N):
        print(ans[row][col] % 1000, end=" ")
    print()