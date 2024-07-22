N, k = map(int, input().split())
x_list = list(map(int, input().split()))

x_list.sort(reverse=True)
limit = x_list[k - 1]

print(limit)