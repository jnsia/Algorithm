def search(x, y):
    m[x][y] = 0

    for e in range(x - 1, x + 2):
        for f in range(y - 1, y + 2):
            if m[e][f] == '*':
                m[x][y] += 1

    if m[x][y] == 0:
        for g in range(x - 1, x + 2):
            for h in range(y - 1, y + 2):
                if m[g][h] == '.':
                    search(g, h)

def printResult():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(m[i][j], end=" ")
        print()

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}', end=" ")

    l1 = []
    global m
    m = []
    count = 0

    for i in range(N + 2):
        l1.append('/')

    for j in range(N + 2):
        m.append(l1[:])

    for x in range(N):
        l = list(map(str, input()))
        
        for y in range(N):
            m[x+1][y+1] = l[y]

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if m[x][y] == '.':
                m[x][y] = 0

                for a in range(x - 1, x + 2):
                    for b in range(y - 1, y + 2):
                        if m[a][b] == '*':
                            m[x][y] += 1

                if m[x][y] == 0:
                    count += 1

                    for c in range(x - 1, x + 2):
                        for d in range(y - 1, y + 2):
                            if m[c][d] == '.':
                                search(c, d)
    
    # printResult()
    # print(count)

    for xx in range(1, N + 1):
        for yy in range(1, N + 1):
            if m[xx][yy] != 0 and m[xx][yy] != '*':

                for w in range(xx - 1, xx + 2):
                    for v in range(yy - 1, yy + 2):
                        if m[w][v] == 0:
                            m[xx][yy] = -1

            if m[xx][yy] != '*' and m[xx][yy] > 0:
                count += 1

    # printResult()
    print(count)