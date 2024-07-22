def recursion(depth, dpd):
    if depth == N:
        print(dpd)
        return

    gk = dpd * 10

    for idx in range(1, 10):
        tmp = gk + idx

        if is_prime(tmp):
            recursion(depth + 1, tmp)


def is_prime(num):
    if num == 1:
        return False

    m = int(num ** 0.5)
    is_true = True

    for mod in range(2, m + 1):
        if num % mod == 0:
            is_true = False

    return is_true


N = int(input())

for glgl in range(1, 10):
    if is_prime(glgl):
        recursion(1, glgl)