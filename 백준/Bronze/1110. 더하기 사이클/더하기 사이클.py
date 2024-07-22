N = input()

if len(N) == 1:
    N = '0' + N

word = N

answer = 1

while True:
    if len(word) == 1:
        word = '0' + word

    temp = str(int(word[0]) + int(word[1]))
    word = word[1] + temp[len(temp) - 1]

    if word == N:
        break

    answer += 1

print(answer)