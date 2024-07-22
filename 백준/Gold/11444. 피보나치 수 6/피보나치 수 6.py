def sol(n):
    global P
    m = (n + 1) // 2

    if n in sol_dict.keys():
        return sol_dict[n]
    else:
        if n % 2 == 0:
            sol_dict[n] = (sol(m) * (sol(m + 1) + sol(m - 1))) % P
        else:
            sol_dict[n] = (sol(m) ** 2 + sol(m - 1) ** 2) % P

        return sol_dict[n] % P

sol_dict = {
    0: 0, 1: 1, 2: 1
}

N = int(input())
P = 1000000007

print(sol(N) % P)
