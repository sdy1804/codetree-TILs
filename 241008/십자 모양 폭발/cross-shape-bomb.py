n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# r,c 값을 받아서 해당 값을 확인
# 해당 값을 포함한 부분들을 0으로 변경
# temp를 활용하여 밑에서부터 채워넣음
# 채워넣은 값을 다시 복사하면 답

def boom(r, c):
    bomb_range = grid[r-1][c-1]
    
    for col_left in range(c-2, c-2-(bomb_range-1), -1): # 왼쪽 터지는 좌표
        # print(r-1, col_left)
        if col_left >= 0:
            grid[r-1][col_left] = 0

    for col_right in range(c, c+(bomb_range-1)): # 오른쪽 터지는 좌표
        # print(r-1, col_right)
        if col_right <= c:
            grid[r-1][col_right] = 0
        
    for row_up in range(r-2, r-2-(bomb_range-1), -1): # 위쪽 터지는 좌표 
        # print(row_up, c-1)
        if row_up >= 0:
            grid[row_up][c-1] = 0
        # print(grid)

    for row_down in range(r, r+(bomb_range-1)): # 아래쪽 터지는 좌표
        # print(row_down, c-1)
        if row_down <= r:
            grid[row_down][c-1] = 0
    
    grid[r-1][c-1] = 0
    # print(grid)

temp_array = [[0] * n for _ in range(n)]


boom(r, c) # 폭탄 폭발

for col in range(n):
    temp_row_idx = n-1
    for row in range(n-1, -1, -1):
        if grid[row][col] != 0:
            temp_array[temp_row_idx][col] = grid[row][col]
            temp_row_idx -= 1

for elem in temp_array:
    for i in elem:
        print(i, end=" ")
    print()