def find_root(in_start, in_end, post_start, post_end):
    if in_start <= in_end and post_start <= post_end:
        idx = inorder.index(postorder[post_end])
        print(inorder[idx], end=' ')

        left_end = idx - in_start
        find_root(in_start, idx - 1, post_start, post_start + left_end - 1)
        find_root(idx + 1, in_end, post_start + left_end, post_end - 1)

import sys
sys.setrecursionlimit(100000)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

find_root(0, N - 1, 0, N - 1)