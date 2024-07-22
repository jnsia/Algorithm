T = int(input())


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = []

    # 파리 배열 초기화
    for _ in range(N):
        temp_list = list(map(int, input().split()))
        arr.append(temp_list)

    max_sum = 0

    # 파리채의 크기를 제외하여 가로 세로 인덱스 N - M 까지 순회
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp_sum = 0

            # 파리채의 크기만큼 순회하면서 temp_sum 값 추가
            for x in range(i, i + M):
                for y in range(j, j + M):
                    temp_sum += arr[x][y]

            # max_sum 비교하여 높을 경우 재할당
            if max_sum <= temp_sum:
                max_sum = temp_sum

    print(f'#{test_case}', max_sum)