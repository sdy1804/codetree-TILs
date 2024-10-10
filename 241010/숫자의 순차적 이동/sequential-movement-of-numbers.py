n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 봐야 하는 숫자를 따로 갱신해야 할 것
# 1. 격자를 순회하여 봐야하는 숫자를 찾는다
# 2. 숫자 근처의 유효한 범위 내에서 가장 큰 좌표를 찾는다
# 3. 해당 좌표의 값과 현재 보고 있는 숫자를 바꾼다
# 4. 봐야하는 숫자 갱신, 숫자가 n*n에 도달하면 1로 변경
# 5. 이를 m번만큼 반복

now_num = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def find_max_val(x, y):
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1] # 상 부터 시계방향
    max_num, max_pos = 0, (0, 0)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y) and grid[next_x][next_y] > max_num:
            max_num = grid[next_x][next_y]
            max_pos = (next_x, next_y)
    return max_pos

def switch_vals(curr_x, curr_y):
    next_x, next_y = find_max_val(curr_x, curr_y)
    # print(next_x, next_y)
    grid[curr_x][curr_y], grid[next_x][next_y] = grid[next_x][next_y], grid[curr_x][curr_y]

def move():
    for r in range(n):
        for c in range(n):
            if grid[r][c] == now_num:
                switch_vals(r, c) 
                # print(grid)
                return grid
                
def simulate():
    global now_num

    for i in range(n*n):
        move()
        # print(grid)
        if now_num == n*n:
            now_num = 1
        else:
            now_num += 1

for _ in range(m):
    simulate()

for elem in grid:
    for i in elem:
        print(i, end=" ")
    print()