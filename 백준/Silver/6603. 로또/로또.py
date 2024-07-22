def comb(arr, collected):
    new_collected = collected[:]

    if len(arr) == 6:
        print(*arr)
        return
    
    for idx in range(length):
        if new_collected[idx] == False:
            new_collected[idx] = True
            comb(arr + [numbers[idx]], new_collected)


while True:
    length, *numbers = map(int, input().split())
    numbers.sort()
    
    if not length:
        break

    collected = [False] * length
    comb([], collected)
    print()