N, M = map(int, input().split())

groups = dict()
singers = dict()

for n in range(N):
    group = input()
    number = int(input())

    groups.setdefault(group, list())

    for i in range(number):
        singer = input()

        groups[group].append(singer)
        singers[singer] = group

for m in range(M):
    quiz = input()
    quiz_type = int(input())

    if quiz_type == 0:
        print(*sorted(groups[quiz]), sep="\n")
    else:
        print(singers[quiz])
