T = int(input())

month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for t in range(1, T + 1):
    print(f'#{t}', end=" ")
    month1, day1, month2, day2 = map(int, input().split())

    days = 1

    if month1 != month2:
        for i in range(month1, month2):
            days += month_day[i]

    days += (day2 - day1)

    print(days)