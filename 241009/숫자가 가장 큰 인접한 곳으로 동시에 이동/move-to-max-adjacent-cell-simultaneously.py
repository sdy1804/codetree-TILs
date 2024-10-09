n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ball_points = [list(map(int, input().split())) for _ in range(m)]

# 1. 격자를 순회하며 구슬이 있는 위치에서 상하좌우의 좌표가 격자 범위 안이고 현재 최대값보다 크면 최대좌표 갱신
# 다만, 최대값이 같은 상태이면 좌표값 갱신하지 않음
# 이를 통해 다음 위치를 계산하여 next_count에 기록
# 2. next_count에서 1이 있는 위치를 ball_points에 새로 기록
# 해당 ball_points에서 다시 반복
# 이를 t만큼 반복
for idx in range(len(ball_points)):
    ball_points[idx][0], ball_points[idx][1] = ball_points[idx][0] - 1, ball_points[idx][1] - 1
# print(ball_points) 

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(ball_point_list):
    next_count = [[0]*n for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for points in range(len(ball_point_list)):
        curr_x, curr_y = ball_point_list[points][0], ball_point_list[points][1]
        for dxs, dys in zip(dx, dy):
            if in_range(curr_x + dxs, curr_y + dys):
                max_point_x, max_point_y = curr_x + dxs, curr_y + dys
        # print(max_point_x, max_point_y)
        for dxs, dys in zip(dx, dy):
            next_x, next_y = curr_x + dxs, curr_y + dys
            if in_range(next_x, next_y) and grid[next_x][next_y] > grid[max_point_x][max_point_y]:
                max_point_x, max_point_y = next_x, next_y
        next_count[max_point_x][max_point_y] += 1
        # print(max_point_x, max_point_y)
    # print(next_count)
    return next_count

count = [[0]*n for _ in range(n)]
for i in range(t):
    # print('ball_points', ball_points)
    count = move(ball_points)
    # print(count)
    ball_points = []
    for r in range(n):
        for c in range(n):
            if count[r][c] == 1:
                ball_points.append([r, c])
# print(ball_points)
print(len(ball_points))