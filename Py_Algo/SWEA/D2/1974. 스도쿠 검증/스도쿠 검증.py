T = int(input())

for test_case in range(1, T + 1):
    result = 1
    arr = []

    # 스도쿠 배열 초기화 및 가로 검증
    for _ in range(0, 9):
        width = set()

        lst = list(map(int, input().split()))
        arr.append(lst)

        # 가로에 있는 모든 숫자를 세트 자료형에 추가
        for x in lst:
            width.add(x)

        # 세트 자료형에 담긴 요소의 개수를 검증
        if len(width) != 9:
            result = 0

    # 스도쿠 배열 세로 검증
    for i in range(0, 9):
    	height = set()

    	for j in range(0, 9):
        	height.add(arr[j][i])

    	if len(height) != 9:
        	result = 0

    # 스도쿠 배열 3x3 사각형 검증
    # 가로 세로 인덱스가 0, 3, 6일 때만 3x3 사각형을 검증
    for a in range(0, 9, 3):
    	for b in range(0, 9, 3):
            square = set()

            # 해당 3x3 사각형 내에 요소들을 세트 자료형에 추가
            for c in range(a, a+3):
                for d in range(b, b+3):
                    square.add(arr[c][d])

            if len(square) != 9:
            	result = 0

    print(f'#{test_case}', result)