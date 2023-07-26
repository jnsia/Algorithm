import sys
input = sys.stdin.readline

N = int(input())

student_list = []

for n in range(N):
    x, y = map(int, input().split())
    student_list.append([x, y])

for i in student_list:
    new_list = [j for j in student_list if j[0] > i[0] and j[1] > i[1]]
    print(len(new_list) + 1, end=" ")