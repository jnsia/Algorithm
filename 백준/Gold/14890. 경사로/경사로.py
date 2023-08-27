def check(arr):
    height_list = []
    now_height = arr[0]
    height_cont = 0

    for idx in range(N):
        if now_height == arr[idx]:
            height_cont += 1

        else:
            if abs(now_height - arr[idx]) > 1:
                return False
            
            height_list.append([now_height, height_cont])
            now_height = arr[idx]
            height_cont = 1

    height_list.append([now_height, height_cont])

    for runway in range(len(height_list)):
        if runway - 1 >= 0 and runway + 1 < len(height_list):
            if height_list[runway][0] < height_list[runway - 1][0] and height_list[runway][0] < height_list[runway + 1][0] and height_list[runway][1] < X * 2:
                return False

        if runway - 1 >= 0 and height_list[runway][0] < height_list[runway - 1][0] and height_list[runway][1] < X:
            return False
        
        if runway + 1 < len(height_list) and height_list[runway][0] < height_list[runway + 1][0] and height_list[runway][1] < X:
            return False
                
    return True


N, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
trans_arr = list(map(list, zip(*arr)))

air_strip = 0

for i in range(N):
    if check(arr[i]):
        air_strip += 1

    if check(trans_arr[i]):
        air_strip += 1

print(air_strip)