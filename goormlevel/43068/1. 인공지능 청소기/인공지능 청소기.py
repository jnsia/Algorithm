T = int(input())

for _ in range(T):
	X, Y, N = map(int, input().split())
	
	sum_xy = abs(X) + abs(Y)
	
	if sum_xy > N or sum_xy % 2 != N % 2:
		print('NO')
	else:
		print('YES')
	