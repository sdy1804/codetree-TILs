n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 범위 안에 존재, 2. 상하좌우의 값들을 보며 현재 값보다 크면 바로 이동
# 이를 반복

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_list = []
curr_x, curr_y = r-1, c-1
max_list.append(grid[curr_x][curr_y])

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def is_bigger():
    for points in range(len(dx)):
        if grid[curr_x + dx[points]][curr_y + dy[points]] > grid[curr_x][curr_y]:
            return True
    return False

while is_bigger():
    for point in range(len(dx)):
        if grid[curr_x + dx[point]][curr_y + dy[point]] > grid[curr_x][curr_y] and in_range(curr_x + dx[point], curr_y + dy[point]):
            # print(grid[curr_x + dx[point]][curr_y + dy[point]])
            max_list.append(grid[curr_x + dx[point]][curr_y + dy[point]])
            curr_x, curr_y = curr_x + dx[point], curr_y + dy[point]
            break

for elem in max_list:
    print(elem, end=" ")