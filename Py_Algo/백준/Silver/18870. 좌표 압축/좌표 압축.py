import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

index_dict = {}

sort_list = sorted(list(set(numbers)))
# print(sort_list)

for idx, value in enumerate(sort_list):
    index_dict[value] = idx
    
# print(index_dict)

for i in range(N):
    numbers[i] = index_dict.get(numbers[i])
    
print(*numbers)