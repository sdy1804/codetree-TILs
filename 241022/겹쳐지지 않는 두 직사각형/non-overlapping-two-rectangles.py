n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 첫번째 직사각형을 고를 때 -> 1*1 부터 n-1 * m-1까지 크기 및 좌표를 바꿔가며 탐색
# 이 중에 합이 최대인 좌표 선택
# 두번째 직사각형 선택 시 -> 마찬가지로 1*1 부터 n-1 * m-1까지 크기 및 좌표를 바꿔가며 탐색하되,
# 만약 첫번째 직사각형과 겹친다면 패스
# 왼쪽 위 좌표를 기준으로 해당 좌표에서 크기를 변경하며 최대값을 구함, visited에 체크하여 중복 방지
# 메인에서 2번씩 좌표를 쭉 돌면서 중복되지 않는 크기에서 최대값을 구함
# 두 최대값을 합침
visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def get_max(lefttop_x, lefttop_y):
    global visited
    total_max = -10000
    lefttop_x_max, lefttop_y_max, rightbot_x_max, rightbot_y_max = 0, 0, 0, 0
    for r in range(0, n-1):
        for c in range(0, m-1):
            now_val = -10000
            now_val = square_sum(lefttop_x, lefttop_y, lefttop_x+r, lefttop_y+c)
            if now_val > total_max:
                lefttop_x_max, lefttop_y_max, rightbot_x_max, rightbot_y_max = lefttop_x, lefttop_y, lefttop_x+r, lefttop_y+c
                visited = [[0 for _ in range(m)] for _ in range(n)]
            total_max = max(now_val, total_max)
    # print(total_max)
    # print(lefttop_x_max, lefttop_y_max, rightbot_x_max, rightbot_y_max)

    for row_point in range(lefttop_x_max, rightbot_x_max+1):
        for col_point in range(lefttop_y, rightbot_y_max+1):
            if in_range(row_point, col_point):
                visited[row_point][col_point] = 1
    # print(visited)
    return total_max, visited

def square_sum(lefttop_x, lefttop_y, rightbot_x, rightbot_y):
    val_sum = 0

    for row_point in range(lefttop_x, rightbot_x+1):
        for col_point in range(lefttop_y, rightbot_y+1):
            if in_range(row_point, col_point):
                val_sum += grid[row_point][col_point]
    return val_sum

def get_max_second(lefttop_x, lefttop_y, vst):
    debuging = [[0 for _ in range(m)] for _ in range(n)]
    total_max = -10000
    lefttop_x_max, lefttop_y_max, rightbot_x_max, rightbot_y_max = 0, 0, 0, 0
    for r in range(0, n):
        for c in range(0, m):
            now_val = -10000
            if check_duplication(lefttop_x, lefttop_y, lefttop_x+r, lefttop_y+c, vst):
                now_val = square_sum(lefttop_x, lefttop_y, lefttop_x+r, lefttop_y+c)
                if now_val > total_max:
                    lefttop_x_max, lefttop_y_max, rightbot_x_max, rightbot_y_max = lefttop_x, lefttop_y, lefttop_x+r, lefttop_y+c
                    debuging = [[0 for _ in range(m)] for _ in range(n)]
                total_max = max(now_val, total_max)
    # print(lefttop_x_max, lefttop_y_max, rightbot_x_max, rightbot_y_max)

    for row_point in range(lefttop_x_max, rightbot_x_max+1):
        for col_point in range(lefttop_y, rightbot_y_max+1):
            if in_range(row_point, col_point):
                debuging[row_point][col_point] = 1
    # print(total_max, debuging)

    return total_max, debuging

def check_duplication(top_x, top_y, bot_x, bot_y, vst):
    for row_point in range(top_x, bot_x+1):
        for col_point in range(top_y, bot_y+1):
            if in_range(row_point, col_point) and vst[row_point][col_point] == 1:
                return False
    return True


first_sqr_max = -10000
visit_first_sqr = [[0 for _ in range(m)] for _ in range(n)]
for row in range(0, n):
    for column in range(0, m):
        now_max = -10000
        now_max, vst = get_max(row, column)
        if now_max > first_sqr_max:
            visit_first_sqr = vst
        first_sqr_max = max(now_max, first_sqr_max)
# print(first_sqr_max, visit_first_sqr)

second_sqr_max = -10000
visit_second_sqr = [[0 for _ in range(m)] for _ in range(n)]
for row in range(0, n):
    for column in range(0, m):
        now_max = -10000
        now_max, vst = get_max_second(row, column, visit_first_sqr)
        if now_max > second_sqr_max:
            visit_second_sqr = vst
        second_sqr_max = max(now_max, second_sqr_max)
# print(second_sqr_max, visit_second_sqr)

print(first_sqr_max + second_sqr_max)