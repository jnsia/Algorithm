N = int(input())
attack = list(map(int, input().split()))
evasion = list(map(int, input().split()))
change = list(map(float, input().split()))
adrenaline = 0

for idx in range(N):
    attack_first = attack[idx] * int(change[idx] * 10) // 10 - evasion[idx]
    evasion_first = attack[idx] - evasion[idx] * int(change[idx] * 10) // 10

    adrenaline += max(attack_first, evasion_first)

print(adrenaline)