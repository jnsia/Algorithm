def power(num, sqr):
    if sqr == 1:
        return num

    next_sqr = power(num, sqr // 2) % mod

    if sqr % 2:
        return (next_sqr * next_sqr * num) % mod
    else:
        return (next_sqr * next_sqr) % mod


M = int(input())

exp_child = 0
exp_parent = 1

mod = 1000000007
answer = 0

for _ in range(M):
    parent, child = map(int, input().split())
    answer += (child * power(parent, mod - 2) % mod) % mod
    answer %= mod

print(answer)


