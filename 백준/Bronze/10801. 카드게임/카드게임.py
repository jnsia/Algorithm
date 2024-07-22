A = list(map(int, input().split()))
B = list(map(int, input().split()))

aw, bw = 0, 0

for i in range(10):
    if A[i] > B[i]:
        aw += 1
    elif A[i] < B[i]:
        bw += 1

if aw == bw:
    print('D')
elif aw > bw:
    print('A')
else:
    print('B')
