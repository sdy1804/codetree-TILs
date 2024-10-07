n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# print(grid)

# ㄴ자는 4가지 케이스 가능, ㅡ자는 2가지 케이스 가능
# 각 케이스 별로 벗어나지 않게 완전탐색, 최대값 적용
# ㄴ자는 왼쪽 위를 기준, 반대 ㄴ은 오른쪽 위를 기준으로 더함
# ㅡ자는 왼쪽을 기준, ㅣ자는 위를 기준으로 더함

def left_down(r, c): # 오른쪽, 아래쪽 튀어나가는 경우
    if r+1 >= n or c+1 >= m:
        return 0
    nums_sum = grid[r][c] + grid[r+1][c] + grid[r+1][c+1]
    return nums_sum

def left_up(r, c): # 오른쪽, 아래쪽
    if r+1 >= n or c+1 >= m:
        return 0
    nums_sum = grid[r][c] + grid[r][c+1] + grid[r+1][c]
    return nums_sum

def right_up(r, c): # 오른쪽, 아래쪽
    if r+1 >= n or c+1 >= m:
        return 0
    nums_sum = grid[r][c] + grid[r][c+1] + grid[r+1][c+1]
    return nums_sum

def right_down(r, c): # 왼쪽, 오른쪽, 아래쪽
    if r+1 >= n or c+1 >= m or c-1 < 0:
        return 0
    nums_sum = grid[r][c] + grid[r+1][c] + grid[r+1][c-1]
    return nums_sum

def straight(r, c): # 오른쪽
    if c+2 >= m:
        return 0
    nums_sum = grid[r][c] + grid[r][c+1] + grid[r][c+2]
    return nums_sum

def straight_vertical(r, c): # 아래쪽
    if r+2 >= n:
        return 0
    nums_sum = grid[r][c] + grid[r+1][c] + grid[r+2][c]
    return nums_sum

ans = 0
for row in range(n):
    for column in range(m):
        left_down_num = left_down(row, column)
        left_up_num = left_up(row, column)
        right_down_num = right_down(row, column)
        right_up_num = right_up(row, column)
        straight_num = straight(row, column)
        straight_vertical_num = straight_vertical(row, column)
        ans = max(left_down_num, left_up_num, right_down_num,right_up_num, straight_num, straight_vertical_num, ans)
print(ans)