N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# 완탐 0 ~ 10
# x좌표를 0~10까지 훑으면서 최대 x값 갯수 세며, 좌표 체크
# y좌표를 0~10까지 훑으면서 최대 y값 갯수 세며, 좌표 체크
# 다시한번 돌면서 남은 좌표들에서 x, y중 최대로 많은 위치로 설정했을 때
# 모든 좌표가 사라지는지 체크


arr2 = arr.copy()

for i in range(2):
    x_max, y_max = False, False
    total_max = 0
    now_max = 0
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
        elif total_max == now_max_y:
            y_point = j
    # print('total_max, x_point, x_max, y_point, y_max', total_max, x_point, x_max, y_point, y_max)
    rmv_list = []
    x_cnt, y_cnt = 0, 0
    for i in range(len(arr2)):
        if arr2[i][0] == x_point:
            x_cnt += 1
        if arr2[i][1] == y_point:
            y_cnt += 1
    if total_max == x_cnt:
        for j in range(len(arr2)):
            if arr2[j][0] == x_point:
                rmv_list.append(arr2[j])
    if total_max == y_cnt:
        for j in range(len(arr2)):
            if arr2[j][1] == y_point:
                rmv_list.append(arr2[j])

    # print('rmv_list', rmv_list)
    for l in range(len(rmv_list)):
        if rmv_list[l] in arr2:
            arr2.remove(rmv_list[l])
    # print('left_arr2', arr2)



all_x = True
for j in range(len(arr2)):
    if arr2[j][0] != arr[0][0]:
        all_x = False
        break
# print(all_x)

all_y = True
for j in range(len(arr2)):
    if arr2[j][1] != arr[0][1]:
        all_y = False
        break
# print(all_y)

if all_x  == True or all_y == True or len(arr2) == 1:
    print(1)
else:
    print(0)