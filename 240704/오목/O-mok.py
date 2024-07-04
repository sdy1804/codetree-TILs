arr = [list(map(int,input().split())) for _ in range(19)]

# 가로, 세로, 대각선으로 1 또는 2가 5개로 나오는지 체크
# 벗어나는지 체크

def in_range(x, y):
    return x >= 0 and x < len(arr) and y >= 0 and y < len(arr)

win_state = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        # 가로
        if in_range(i, j+1) and in_range(i, j+2) and in_range(i, j+2) and in_range(i, j+2):
            if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1 and arr[i][j+3] == 1 and arr[i][j+4] == 1:
                win_state = 1
                center_x, center_y = i+1, j+2+1
            elif arr[i][j] == 2 and arr[i][j+1] == 2 and arr[i][j+2] == 2 and arr[i][j+3] == 2 and arr[i][j+4] == 2:
                win_state = 2
                center_x, center_y = i+1, j+2+1
        # 세로
        if in_range(i+1, j) and in_range(i+2, j) and in_range(i+3, j) and in_range(i+4, j):
            if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+2][j] == 1 and arr[i+3][j] == 1 and arr[i+4][j] == 1:
                win_state = 1
                center_x, center_y = i+2+1, j+1
            elif arr[i][j] == 2 and arr[i+1][j] == 2 and arr[i+2][j] == 2 and arr[i+3][j] == 2 and arr[i+4][j] == 2:
                win_state = 2
                center_x, center_y = i+2+1, j+1
        # 대각선
        if (in_range(i+1, j+1) and in_range(i+2, j+2) and in_range(i+3, j+3) and in_range(i+4, j+4)) or (in_range(i+1, j-1) and in_range(i+2, j-2) and in_range(i+3, j-3) and in_range(i+4, j-4)):
            if arr[i][j] == 1 and arr[i+1][j+1] == 1 and arr[i+2][j+2] == 1 and arr[i+3][j+3] == 1 and arr[i+4][j+4] == 1:
                win_state = 1
                center_x, center_y = i+2+1, j+2+1
            elif arr[i][j] == 2 and arr[i+1][j+1] == 2 and arr[i+2][j+2] == 2 and arr[i+3][j+3] == 2 and arr[i+4][j+4] == 2:
                win_state = 2
                center_x, center_y = i+2+1, j+2+1
            elif arr[i][j] == 1 and arr[i+1][j-1] == 1 and arr[i+2][j-2] == 1 and arr[i+3][j-3] == 1 and arr[i+4][j-4] == 1:
                win_state = 1
                center_x, center_y = i+2+1, j-2+1
            elif arr[i][j] == 2 and arr[i+1][j-1] == 2 and arr[i+2][j-2] == 2 and arr[i+3][j-3] == 2 and arr[i+4][j-4] == 2:
                win_state = 2
                center_x, center_y = i+2+1, j-2+1

if win_state == 0:
    print(win_state)
elif win_state == 1:
    print(win_state)
    print(center_x, center_y)
elif win_state == 2:
    print(win_state)
    print(center_x, center_y)