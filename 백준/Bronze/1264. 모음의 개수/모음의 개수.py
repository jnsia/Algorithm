aeiou = ['a', 'e', 'i', 'o', 'u']

while True:
    words = input()

    if words == '#':
        break

    cnt = 0

    for word in words:
        word = word.lower()

        if word in aeiou:
           cnt += 1

    print(cnt)