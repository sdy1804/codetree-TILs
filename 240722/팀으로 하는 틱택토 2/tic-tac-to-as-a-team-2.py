arr = [list(input()) for _ in range(3)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])
# print(arr)

# 가로, 세로, 대각선에서 임시 리스트에 붙여넣었을 때 len이 2면 OK
ans = 0

row_list = []
for i in range(len(arr)): # 가로
    temp_list = []
    for j in range(len(arr[i])):
        if arr[i][j] not in temp_list:
            temp_list.append(arr[i][j])
    # print(temp_list)
    if len(temp_list) == 2:
        ans += 1
    row_list.append(temp_list)
# print(row_list)
# print(ans)

column_list = []
for i in range(len(arr)): # 세로
    temp_list = []
    for j in range(len(arr[i])):
        if arr[j][i] not in temp_list:
            temp_list.append(arr[j][i])
    # print(temp_list)
    if len(temp_list) == 2 and temp_list not in row_list and temp_list not in column_list:
        # print('not in row')
        ans += 1
    column_list.append(temp_list)
# print(column_list)
# print(ans)

diagonal_list = []
temp_list = []
for i in range(len(arr)): # 대각선
    if arr[i][i] not in temp_list:
            temp_list.append(arr[i][i])
# print(temp_list)
if len(temp_list) == 2 and temp_list not in row_list and temp_list not in column_list:
    ans += 1
diagonal_list.append(temp_list)

temp_list = []
for j in range(len(arr[i]) - 1, -1, -1):
    i = abs(j - 2)
    # print(i, j)
    if arr[i][j] not in temp_list:
        temp_list.append(arr[i][j])
# print(temp_list)
if len(temp_list) == 2 and temp_list not in row_list and temp_list not in column_list and temp_list not in diagonal_list:
    ans += 1
print(ans)
diagonal_list.append(temp_list)
# print(diagonal_list)