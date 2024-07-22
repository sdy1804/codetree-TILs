N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# 완탐 0 ~ 10
# x좌표를 0~10까지 훑으면서 최대 x값 갯수 세며, 좌표 체크
# y좌표를 0~10까지 훑으면서 최대 y값 갯수 세며, 좌표 체크
# 다시한번 돌면서 남은 좌표들에서 x, y중 최대로 많은 위치로 설정했을 때
# 모든 좌표가 사라지는지 체크

total_max_x = 0
x_point = 0
for i in range(11):
    now_max_x = 0
    for j in range(len(arr)):
        if arr[j][0] == i:
            now_max_x += 1
    total_max_x = max(now_max_x, total_max_x)
    if total_max_x == now_max_x:
        x_point = i
# print(total_max_x, x_point)

arr2 = arr.copy()

for i in range(len(arr)):
    if arr[i][0] == x_point:
        arr2.remove(arr[i])
# print(arr2)

total_max_y = 0
y_point = 0
for i in range(11):
    now_max_y = 0
    for j in range(len(arr2)):
        if arr2[j][1] == i:
            now_max_y += 1
    total_max_y = max(now_max_y, total_max_y)
    if total_max_y == now_max_y:
        y_point = i
# print(total_max_y, y_point)

for i in range(len(arr)):
    if arr[i][1] == y_point:
        arr2.remove(arr[i])
# print(arr2)

all_x, all_y = True, True
for i in range(len(arr2)):
    temp_x = arr2[0][0]
    temp_y = arr2[0][1]
    # print(temp_x, temp_y)
    if arr2[i][0] != temp_x:
        all_x = False
    if arr2[i][0] != temp_y:
        all_y = False
if all_x == False and all_y == False:
    print(0)
else:
    print(1)