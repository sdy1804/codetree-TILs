arr = [list(input()) for _ in range(10)]
# print(arr)
# R이 가로막는 경우 - 세로, 가로로 일렬일 때 -> 옆으로 나와서 L과 B의 거리만큼 이동하면 됨
# => L과 B의 인덱스의 차이+1
#
# R이 문제되지 않는 경우 - 가로, 세로로 일렬이 아닐 때 -> B와 L의 인덱스 위치를 통해 계산 가능
# => 세로 = B와 L의 행 인덱스 차이 / 가로 = 열 인덱스 차이-1
# R이 문제되지 않는 경우 - 가로, 세로로 일렬일 때 -> B와 L의 인덱스 위치를 통해 계산 가능
# => 세로 = B와 L의 행 인덱스 차이 / 가로 = 열 인덱스 차이


for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            B_row, B_column = i, j
        if arr[i][j] == 'R':
            R_row, R_column = i, j
        if arr[i][j] == 'L':
            L_row, L_column = i, j
# print(B_row, B_column)
# print(R_row, R_column)
# print(L_row, L_column)
ans = 0
if (B_column < R_column < L_column or B_column > R_column > L_column) and B_row == R_row == L_row:
    ans = abs(B_column - L_column) + 1
elif (B_row < R_row < L_row or B_row > R_row > L_row) and B_column == R_column == L_column:
    ans = abs(B_row - L_row) + 1
elif B_row == L_row:
    ans = abs(B_column - L_column - 1)
elif B_column == L_column:
    ans = abs(B_row - L_row - 1)
else:
    ans = abs(B_row - L_row) + (abs(B_column - L_column) - 1)
print(ans)