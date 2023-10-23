def gcd(x, y):
    if x < y:
        x, y = y, x

    while y:
        x, y = y, x % y

    return x


def power(num, sqr):
    if sqr == 0:
        return 0

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

for _ in range(M):
    parent, child = map(int, input().split())
    exp_child = exp_parent * child + parent * exp_child
    exp_parent = exp_parent * parent

tmp_gcd = gcd(exp_parent, exp_child)
exp_child = exp_child // tmp_gcd
exp_parent = exp_parent // tmp_gcd

answer = (exp_child * power(exp_parent, mod - 2)) % mod
print(answer)


