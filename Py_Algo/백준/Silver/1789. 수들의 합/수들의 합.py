number = int(input())
a_list = []
i = 1
while i <= number:
    a_list.append(i)
    number -= i
    i += 1
print(i - 1)