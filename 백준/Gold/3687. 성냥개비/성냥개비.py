N = int(input())

for _ in range(N):
    num = int(input())
    
    max_ans = ''
    min_ans = ''
    
    if num % 2:
        max_ans = '7' + '1' * (num // 2 - 1)
    else:
        max_ans = '1' * (num // 2)
    
    ans = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    
    if num <= 10:
        min_ans = ans[num]
    else:
        if num % 7 == 0:
            min_ans = '8'*(num//7)
        elif num % 7 == 1:
            min_ans = '10'+ '8'*(num//7 - 1)
        elif num % 7 == 2:
            min_ans = '1' + '8' * (num // 7)
        elif num % 7 == 3:
            min_ans = '200' + '8' * (num // 7 - 2)
        elif num % 7 == 4:
            min_ans = '20' + '8' * (num // 7 - 1)
        elif num % 7 == 5:
            min_ans = '2' + '8' * (num // 7)
        elif num % 7 == 6:
            min_ans = '6' + '8' * (num // 7)

    print(min_ans, end=" ")
    print(max_ans)