N = int(input())

state_dict = dict()

for i in range(N):
    num = int(input())

    state_dict.setdefault(num, 0)
    state_dict[num] += 1

max_key = 2 ** 62 + 1
max_value = 0

for k, v in state_dict.items():
    if max_value < v:
        max_value = v
        max_key = k
    elif max_value == v:
        max_key = min(k, max_key)


print(max_key)
