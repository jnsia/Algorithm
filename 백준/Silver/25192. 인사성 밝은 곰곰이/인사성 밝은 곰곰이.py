N = int(input())

chated_user = set()
gomgom = 0

for i in range(N):
    chat = input()

    if chat == 'ENTER':
        chated_user.clear()
    elif chat not in chated_user:
        gomgom += 1
        chated_user.add(chat)

print(gomgom)