N = int(input())

numbers = []

for i in range(N):
    numbers.append(int(input()))
    
print(*sorted(numbers), sep="\n")