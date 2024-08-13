N, D = map(int, input().split())
ants = list(map(int, input().split()))

ants.sort()

i = 0
j = 0

answer = N

while i < N and j < N:
	min_ant = ants[i]
	max_ant = ants[j]
	
	if i == j:
		j += 1
	
	if max_ant - min_ant > D:
		i += 1
	else:
		j += 1
		answer = min(answer, N - (j - i))

print(answer)