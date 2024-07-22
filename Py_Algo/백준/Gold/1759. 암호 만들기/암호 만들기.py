def check(string):
    result = False
    aeiou_cnt = 0

    for i in string:
        if i in aeiou:
            aeiou_cnt += 1

    if aeiou_cnt > 0 and L - aeiou_cnt > 1:
        result = True

    return result


def comb(res, depth):
    if depth == C:
        if len(res) == L and check(res):
            print(res)
        return

    comb(res + arr[depth], depth + 1)
    comb(res, depth + 1)


L, C = map(int, input().split())
arr = sorted(input().split())
aeiou = 'aeiou'
comb("", 0)
