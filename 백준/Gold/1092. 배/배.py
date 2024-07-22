N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cranes_end = N
box_cnt = 0

answer = 0

if max(boxes) > max(cranes):
    print(-1)
else:
    while box_cnt < M:

        for crane_idx in range(cranes_end):
            crane = cranes[crane_idx]

            res = False

            for box_idx in range(M - box_cnt):
                box = boxes[box_idx]

                if box <= crane and box != 0:
                    boxes[box_idx] = 0
                    box_cnt += 1
                    boxes.sort(reverse=True)
                    res = True
                    break

            if not res:
                cranes_end -= 1

        answer += 1

    print(answer)
