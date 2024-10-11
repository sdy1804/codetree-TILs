n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# print(grid)

ans = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

order = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y): # 유효하지 않은 범위일 때
        return False
    
    if visited[x][y] or grid[x][y] == 0: # 이미 방문한 곳이거나 뱀이 있을 때
        return False
    return True

def DFS(x, y):
    global order

    dxs, dys = [1, 0], [0, 1]
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        if can_go(next_x, next_y):
            ans[next_x][next_y] = order
            order += 1
            visited[next_x][next_y] = 1
            DFS(next_x, next_y)

DFS(0, 0)
# print(ans)
# print(ans[n-1][m-1])
if ans[n-1][m-1] != 0:
    print(1)
else:
    print(0)