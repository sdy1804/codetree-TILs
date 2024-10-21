n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 움직일 수 있는 모든 케이스 커버 해야 함
# 시작점은 항상 중심좌표의 한 행 아래
# 방법 1. 시작점은 항상 동일. 1번째 순회 종료지점이 가능한 지점은 5*5일 때 3번, 4*4일때 2번, 3*3일 때 1번이므로 최대 n-2만큼 이동가능
# 2번째 종료지점도 최대 n-2번만큼 범위내에 있을 경우 이동
# ex) for문 1번순회 째 -> 1번 이동 시 -> for문 2번째순회 1번 이동, 3번째순회는 1번째순회 이동한만큼, 4번째순회는 2번째순회 이동한만큼 이동
# ex) for문 1번 째 -> 1번 이동, for문 2번째 2번 이동, 마찬가지...

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max(center_x, center_y, grid):
    total_max = 0
    start_x, start_y = center_x+1, center_y

    for fst_up in range(1, n-2+1):
        for scd_up in range(1, n-2+1):
            now_max = 0
            right_up_x, right_up_y = start_x - fst_up, start_y + fst_up
            left_up_x, left_up_y = right_up_x - scd_up, right_up_y - scd_up
            left_down_x, left_down_y = left_up_x + fst_up, left_up_y - fst_up
            right_down_x, right_down_y = left_down_x + scd_up, left_down_y + scd_up

            if in_range(right_up_x, right_up_y) and in_range(left_up_x, left_up_y) \
            and in_range(left_down_x, left_down_y) and in_range(right_down_x, right_down_y):
                now_max = cal_by_points(left_up_x, left_up_y, right_down_x, right_down_y, left_down_x, left_down_y, right_up_x, right_up_y, grid)
                total_max = max(now_max, total_max)
    return total_max

def cal_by_points(top_x, top_y, down_x, down_y, left_x, left_y, right_x, right_y, grid):
    value_sum = 0

    x_sum, y_sum = down_x - 1, down_y + 1
    for t in range(down_x-1, right_x, -1):
        value_sum += grid[x_sum][y_sum]
        x_sum, y_sum = x_sum - 1, y_sum + 1
    
    x_sum, y_sum = right_x - 1, right_y - 1
    for t in range(right_x - 1, top_x, -1):
        value_sum += grid[x_sum][y_sum]
        x_sum, y_sum = x_sum - 1, y_sum - 1
    
    x_sum, y_sum = top_x + 1, top_y - 1
    for t in range(top_x + 1, left_x):
        value_sum += grid[x_sum][y_sum]
        x_sum, y_sum = x_sum + 1, y_sum - 1
    
    x_sum, y_sum = left_x + 1, left_y + 1
    for t in range(left_x + 1, down_x):
        value_sum += grid[x_sum][y_sum]
        x_sum, y_sum = x_sum + 1, y_sum + 1
    
    value_sum += grid[top_x][top_y] + grid[down_x][down_y] + grid[left_x][left_y] + grid[right_x][right_y]
    return value_sum

ans = 0
for row in range(1, n-1):
    for column in range(1, n-1):
        now_val = find_max(row, column, grid)
        ans = max(now_val, ans)
print(ans)