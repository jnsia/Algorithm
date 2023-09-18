N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    nums = sorted([min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])])
    first = nums[0]
    second = nums[0] + nums[1]
    third = sum(nums)

    vertex = third * 4
    edge =  second * (N - 1) * 4 + second * (N - 2) * 4
    plane = first * (N - 2) * (N - 1) * 4 + first * (N - 2) * (N - 2)

    print(vertex + edge + plane)