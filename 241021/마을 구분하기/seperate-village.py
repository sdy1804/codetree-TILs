n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# dfs를 통해서 마을마다 값을 갱신
# 1의 갯수를 카운팅하면 마을의 수 카운트 가능
# max order 값들을 기록하며, 마을 바뀔 시 갱신

ans = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

order = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if grid[x][y] == 0 or visited[x][y] == 1:
        return False
    return True

def DFS(x, y):
    global order
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if can_go(next_x, next_y):
            ans[next_x][next_y] = order
            order += 1
            visited[next_x][next_y] = 1
            DFS(next_x, next_y)

order_list = []
for row in range(n):
    for column in range(n):
        if ans[row][column] == 0 and grid[row][column] == 1:
            order = 1
            ans[row][column] = order
            order += 1
            visited[row][column] = 1
            DFS(row, column)
            if order == 1:
                order_list.append(order)
            else:
                order_list.append(order-1)
order_list.sort()
# print(ans)

country_num = 0
for row in range(n):
    for column in range(n):
        if ans[row][column] == 1:
            country_num += 1
print(country_num)
for elem in order_list:
    print(elem)