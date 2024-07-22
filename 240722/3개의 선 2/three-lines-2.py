N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# 완탐 0 ~ 10
# x좌표를 0~10까지 훑으면서 최대 x값 갯수 세며, 좌표 체크
# y좌표를 0~10까지 훑으면서 최대 y값 갯수 세며, 좌표 체크
# 다시한번 돌면서 남은 좌표들에서 x, y중 최대로 많은 위치로 설정했을 때
# 모든 좌표가 사라지는지 체크

total_max = 0
x_point = 0
y_point = 0
arr2 = arr.copy()

for i in range(2):
    x_max, y_max = False, False
    for j in range(11):
        now_max_x = 0
        now_max_y = 0
        for k in range(len(arr)):
            if arr[k][0] == i:
                now_max_x += 1
            if arr[k][1] == i:
                now_max_y += 1
        # print('i, now_max_x, now_max_y', i, now_max_x, now_max_y)
        total_max = max(now_max_x, now_max_y, total_max)
        if total_max == now_max_x:
            x_point = i
            x_max = True
        elif total_max == now_max_y:
            y_point = i
            y_max = True
    rmv_list = []
    for l in range(len(arr2)):
        if x_max == True:
            if arr2[l][0] == x_point:
                rmv_list.append(arr2[l])
        elif y_max == True:
            if arr2[l][1] == y_point:
                rmv_list.append(arr2[l])
    # print('rmv_list', rmv_list)
    for l in range(len(rmv_list)):
        if rmv_list[l] in arr2:
            arr2.remove(rmv_list[l])
    # print(arr2)

all_same = False
for i in range(len(arr2)):
    if len(arr2) == 1 or arr[i][0] == arr[0][0] or arr[i][1] == arr[0][1]:
        all_same = True
if all_same == True:
    print(1)
else:
    print(0)