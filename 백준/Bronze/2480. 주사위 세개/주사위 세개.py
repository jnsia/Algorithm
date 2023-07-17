A, B, C = map(int, input().split())

sum = 0

if A == B == C:
    sum += 10000
    sum += A * 1000
elif A == B or A == C:
    sum += 1000
    sum += A * 100
elif B == C:
    sum += 1000
    sum += C * 100
else:
    sum += max(A, B, C) * 100

print(sum)