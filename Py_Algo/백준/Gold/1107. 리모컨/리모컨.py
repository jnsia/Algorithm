N = int(input())
M = int(input())

if M > 0:
    break_down = list(map(str, input().split()))
else:
    break_down = []

res = abs(N - 100)

for channel in range(1000001):
    is_false = False

    for number in str(channel):
        if number in break_down:
            is_false = True
            break
            
    if is_false:
        continue
    else:
        res = min(abs(N - channel) + len(str(channel)), res)

print(res)
        