def binary_search():
    low = 1
    high = int(1e18)
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        result = challenge(mid)

        if result:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


def challenge(max_hp):
    cur_hp = max_hp
    cur_power = ATK

    is_possible = True

    for floor in range(N):
        if not is_possible:
            break

        type, power, health = dungeon[floor]

        if type == 1:
            turns = health // cur_power - 1

            if health % cur_power:
                turns += 1

            cur_hp -= power * turns

            if cur_hp <= 0:
                is_possible = False
                break

        elif type == 2:
            cur_hp = min(cur_hp + health, max_hp)
            cur_power += power

    return is_possible


N, ATK = map(int, input().split())

dungeon = []

for _ in range(N):
    T, A, H = map(int, input().split())
    dungeon.append((T, A, H))

print(binary_search())