def time_convert(time: str):
    hour, minute = time.split(':')

    return int(hour) * 60 + int(minute)


S, E, Q = input().split()

start_time: int = time_convert(S)
end_time: int = time_convert(E)
end_streaming: int = time_convert(Q)

enter_people = set()
exit_people = set()

while True:
    try:
        time, nickname = input().split()
        chat_time = time_convert(time)

        if chat_time <= start_time:
            enter_people.add(nickname)

        if end_time <= chat_time <= end_streaming:
            exit_people.add(nickname)
    except:
        break

result = enter_people.intersection(exit_people)

print(len(result))