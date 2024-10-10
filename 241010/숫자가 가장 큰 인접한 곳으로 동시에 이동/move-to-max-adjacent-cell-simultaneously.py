n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# ball_points = [list(map(int, input().split())) for _ in range(m)]

# for idx in range(len(ball_points)): # 0,0 기준의 좌표로 변경
#     ball_points[idx][0], ball_points[idx][1] = ball_points[idx][0] - 1, ball_points[idx][1] - 1
# print(ball_points) 

# Step 1. next_count 초기화
# Step 2. count를 순회하면서 1이 있는 좌표일 경우
# 상하좌우 순회, 격자 안에 존재하면서 max값보다 큰 값일 경우만 max 및 좌표 갱신
# Step 3. 갱신된 좌표를 next_count에 기록
# Step 4. 이것을 count에 옮긴 후, 2보다 큰 값은 0으로 변경
# 이것을 t만큼 반복

count = [[0]*n for _ in range(n)]
next_count = [[0]*n for _ in range(n)]

def in_range(x, y): # 유의미한 좌표인지 확인
    return x >= 0 and x < n and y >= 0 and y < n

def max_points(x, y): # 격자 순회하면서 최대값 좌표 찾는 함수
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num, max_pos = 0, (0, 0)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y) and grid[next_x][next_y] > max_num:
            max_num = grid[next_x][next_y]
            max_pos = (next_x, next_y)
    return max_pos

def apply_to_next(x, y): # 갱신된 좌표 기록
    next_x, next_y = max_points(x, y)
    next_count[next_x][next_y] += 1

def remove_duplicate_pos(): # 겹치는 구슬 없애는 함수
    for r in range(n):
        for c in range(n):
            if count[r][c] >= 2:
                count[r][c] = 0

def move_all():
    for r in range(n): # next_count 초기화
        for c in range(n):
            next_count[r][c] = 0
    
    for r in range(n): # 구슬 위치 확인하면서 next_count 기록
        for c in range(n):
            if count[r][c] == 1:
                apply_to_next(r, c)
    
    for r in range(n): # count 갱신
        for c in range(n):
            count[r][c] = next_count[r][c]

def simulate():
    move_all()
    remove_duplicate_pos()

for _ in range(m):
    x, y = list(map(int, input().split()))
    count[x-1][y-1] = 1

for _ in range(t):
    simulate()

ans = 0
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            ans += 1
print(ans)