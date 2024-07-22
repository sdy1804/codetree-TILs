N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# 완탐 0 ~ 10
# x좌표를 0~10까지 훑으면서 최대 x값 갯수 세며, 좌표 체크
# y좌표를 0~10까지 훑으면서 최대 y값 갯수 세며, 좌표 체크
# 다시한번 돌면서 남은 좌표들에서 x, y중 최대로 많은 위치로 설정했을 때
# 모든 좌표가 사라지는지 체크


arr2 = arr.copy()

for i in range(3):
    x_max, y_max = False, False
    total_max = 0
    x_point = 0
    y_point = 0
    for j in range(11):
        now_max_x = 0
        now_max_y = 0
        for k in range(len(arr2)):
            if arr2[k][0] == j:
                now_max_x += 1
            if arr2[k][1] == j:
                now_max_y += 1
        # print('j, now_max_x, now_max_y', j, now_max_x, now_max_y)
        total_max = max(now_max_x, now_max_y, total_max)
        # print('total_max', total_max)
        if total_max == now_max_x:
            x_point = j
            x_max = True
        elif total_max == now_max_y:
            y_point = j
            y_max = True
    # print('total_max, x_point, x_max, y_point, y_max', total_max, x_point, x_max, y_point, y_max)
    rmv_list = []
    for l in range(len(arr2)):
        if x_max == True:
            if arr2[l][0] == x_point:
                rmv_list.append(arr2[l])
        if y_max == True:
            if arr2[l][1] == y_point:
                rmv_list.append(arr2[l])
    # print('rmv_list', rmv_list)
    for l in range(len(rmv_list)):
        if rmv_list[l] in arr2:
            arr2.remove(rmv_list[l])
    # print(arr2)

one_more_left = False
if len(arr2) == 0 or len(arr2) == 1:
    one_more_left = False
else:
    one_more_left = True

if one_more_left:
    print(0)
else:
    print(1)