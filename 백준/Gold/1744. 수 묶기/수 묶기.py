N = int(input())
negative = []
positive = []

res = 0

for _ in range(N):
    number = int(input())

    if number > 0:
        positive.append(number)
    else:
        negative.append(number)

negative.sort(reverse=True)
positive.sort()

while len(negative) > 1:
    a = negative.pop()
    b = negative.pop()

    res += max(a * b, a + b)


while len(positive) > 1:
    a = positive.pop()
    b = positive.pop()

    res += max(a * b, a + b)

if negative and positive:
    a = negative.pop()
    b = positive.pop()

    res += max(a * b, a + b)
elif negative:
    res += negative.pop()
elif positive:
    res += positive.pop()

print(res)