for t in range(1,int(input())+1):
    c=0
    for bit in input():
        if int(bit)!=(c%2): c+=1
    print(f'#{t} {c}')