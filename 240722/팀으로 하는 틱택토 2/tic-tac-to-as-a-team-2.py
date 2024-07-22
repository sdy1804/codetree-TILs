arr = [list(input()) for _ in range(3)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])
# print(arr)

# 가로, 세로, 대각선에서 임시 리스트에 붙여넣었을 때 len이 2면 OK
ans = 0

for i in range(len(arr)): # 가로
    temp_list = []
    for j in range(len(arr[i])):
        if arr[i][j] not in temp_list:
            temp_list.append(arr[i][j])
    # print(temp_list)
    if len(temp_list) == 2:
        ans += 1
# print(ans)

for i in range(len(arr)): # 세로
    temp_list = []
    for j in range(len(arr[i])):
        if arr[j][i] not in temp_list:
            temp_list.append(arr[j][i])
    # print(temp_list)
    if len(temp_list) == 2:
        ans += 1
# print(ans)

temp_list = []
for i in range(len(arr)): # 대각선
    if arr[i][i] not in temp_list:
            temp_list.append(arr[i][i])
# print(temp_list)
if len(temp_list) == 2:
    ans += 1

temp_list = []
for j in range(len(arr[i]) - 1, -1, -1):
    i = abs(j - 2)
    # print(i, j)
    if arr[i][j] not in temp_list:
        temp_list.append(arr[i][j])
# print(temp_list)
if len(temp_list) == 2:
    ans += 1
print(ans)