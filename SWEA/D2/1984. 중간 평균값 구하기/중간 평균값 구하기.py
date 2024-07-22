T = int(input())

for t in range(1, T + 1):
    l = list(map(int, input().split()))

    l.remove(min(l))
    l.remove(max(l))

    print(f'#{t}', round(sum(l)/len(l)))