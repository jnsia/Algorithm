N = input()

numbers = list(N)
numbers.sort(reverse=True)

result = ''

for i in numbers:
    result += i
    
print(int(result))